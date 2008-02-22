# -*- coding: utf-8 -*-
# vim: expandtab ts=4 sw=4 sts=4:
#
# Copyright (C) 2007 GNS-3 Dev Team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# Contact: contact@gns3.net
#

import time
import GNS3.Globals as globals
from socket import socket, timeout, AF_INET, SOCK_STREAM
from PyQt4 import QtCore, QtGui
from GNS3.Utils import translate, debug
from GNS3.Node.IOSRouter import IOSRouter

class HypervisorManager:
    """ HypervisorManager class
        Start one or more dynamips in hypervisor mode
    """

    def __init__(self):
    
        self.hypervisors = []
        self.setDefaults()
        
    def __del__(self):
        """ Shutdown all started hypervisors 
        """

        self.stopProcHypervisors()
       
    def setDefaults(self):
        """ Set the default values for the hypervisor manager
        """
        
        dynamips = globals.GApp.systconf['dynamips']
        self.hypervisor_path = dynamips.path
        self.hypervisor_wd = dynamips.workdir
        self.baseConsole = dynamips.baseConsole
        globals.hypervisor_baseport = dynamips.port
        globals.GApp.dynagen.globaludp = dynamips.baseUDP
      
    def startNewHypervisor(self, port):
        """ Create a new dynamips process and start it
        """

        proc = QtCore.QProcess(globals.GApp.mainWindow)
        if self.hypervisor_wd:
            # set the working directory
            proc.setWorkingDirectory(self.hypervisor_wd)
            
        # test if an hypervisor is already running on this port
        s = socket(AF_INET, SOCK_STREAM)
        s.setblocking(0)
        s.settimeout(300)
        try:
            s.connect(('localhost', port))
            QtGui.QMessageBox.warning(globals.GApp.mainWindow, 'Hypervisor Manager',  unicode(translate("HypervisorManager", "Hypervisor already running on port %i")) % port) 
            s.close()
            globals.hypervisor_baseport += 1
            return None
        except:
            s.close()

        # start dynamips in hypervisor mode (-H)
        proc.start(self.hypervisor_path,  ['-H', str(port)])

        if proc.waitForStarted() == False:
            QtGui.QMessageBox.critical(globals.GApp.mainWindow, 'Hypervisor Manager',  unicode(translate("HypervisorManager", "Can't start Dynamips on port %i")) % port)
            return None

        hypervisor = {'port': port,
                            'proc_instance': proc, 
                            'load': 0}

        self.hypervisors.append(hypervisor)
        return hypervisor
    
    def waitHypervisor(self, hypervisor):
        """ Wait the hypervisor until it accepts connections
        """

        # give 15 seconds to the hypervisor to accept connections
        count = 15
        progress = None
        connection_success = False
        debug("Hypervisor manager: connect on " + str(hypervisor['port']))
        for nb in range(count + 1):
            s = socket(AF_INET, SOCK_STREAM)
            s.setblocking(0)
            s.settimeout(300)
            if nb == 3:
                progress = QtGui.QProgressDialog(unicode(translate("HypervisorManager", "Connecting to an hypervisor on port %i ...")) % hypervisor['port'], 
                                                                                                                                        translate("HypervisorManager", "Abort"), 0, count, globals.GApp.mainWindow)
                progress.setMinimum(1)
                progress.setWindowModality(QtCore.Qt.WindowModal)
                globals.GApp.processEvents(QtCore.QEventLoop.AllEvents | QtCore.QEventLoop.WaitForMoreEvents, 2000)
            if nb > 2:
                progress.setValue(nb)
                globals.GApp.processEvents(QtCore.QEventLoop.AllEvents | QtCore.QEventLoop.WaitForMoreEvents, 2000)
                if  progress.wasCanceled():
                    progress.reset()
                    break
            try:
                s.connect(('localhost', hypervisor['port']))
            except:
                s.close()
                time.sleep(1)
                continue
            debug("Hypervisor manager: hypervisor on port " +  str(hypervisor['port']) + " started")
            connection_success = True
            break

        if connection_success:
            s.close()
            globals.hypervisor_baseport += 1
            time.sleep(0.2)
        else:
            QtGui.QMessageBox.critical(globals.GApp.mainWindow, 'Hypervisor Manager',  
                                       unicode(translate("HypervisorManager", "Can't connect to the hypervisor on port %i")) % hypervisor['port'])
            hypervisor['proc_instance'].close()
            self.hypervisors.remove(hypervisor)
            return False
        if progress:
            progress.setValue(count)
            progress.deleteLater()
            progress = None
        return True

    def allocateHypervisor(self, node):
        """ Allocate an hypervisor for a given node
        """

        for hypervisor in self.hypervisors:
            if not isinstance(node, IOSRouter) or hypervisor['load'] + node.default_ram <= globals.GApp.systconf['dynamips'].memory_limit:
                if isinstance(node, IOSRouter):
                    hypervisor['load'] += node.default_ram
                debug('Hypervisor manager: allocates an already started hypervisor (port: ' + str(hypervisor['port']) + ')')
                dynamips_hypervisor = globals.GApp.dynagen.dynamips['localhost:' + str(hypervisor['port'])]
                node.set_hypervisor(dynamips_hypervisor)
                return hypervisor

        hypervisor = self.startNewHypervisor(globals.hypervisor_baseport)
        if hypervisor == None:
            return None

        if not self.waitHypervisor(hypervisor):
            return None

        if isinstance(node, IOSRouter):
            hypervisor['load'] = node.default_ram
        dynamips_hypervisor = globals.GApp.dynagen.create_dynamips_hypervisor('localhost', hypervisor['port'])
        debug("Hypervisor manager: create a new hypervisor on port " + str(hypervisor['port']))
        globals.GApp.dynagen.update_running_config()
        dynamips_hypervisor.configchange = True
        dynamips_hypervisor.udp = globals.GApp.dynagen.globaludp
        dynamips_hypervisor.starting_udp = globals.GApp.dynagen.globaludp
        dynamips_hypervisor.baseconsole = self.baseConsole
        # use project workdir in priority
        if globals.GApp.workspace.projectWorkdir:
            dynamips_hypervisor.workingdir = globals.GApp.workspace.projectWorkdir
        elif self.hypervisor_wd:
            dynamips_hypervisor.workingdir = self.hypervisor_wd
        globals.GApp.dynagen.globaludp += globals.GApp.systconf['dynamips'].udp_incrementation
        node.set_hypervisor(dynamips_hypervisor)
        return hypervisor

    def unallocateHypervisor(self, node, port):
        """ Unallocate an hypervisor for a given node
        """

        for hypervisor in self.hypervisors:
            if hypervisor['port'] == int(port):
                debug("Hypervisor manager: unallocate hypervisor (port: " + str(port) + ") for node " + node.hostname)
                hypervisor['load'] -= node.default_ram
                if hypervisor['load'] <= 0:
                    hypervisor['load'] = 0
                break
    
    def getHypervisor(self, port):
        """ Get an hypervisor from the hypervisor manager
        """

        for hypervisor in self.hypervisors:
            if hypervisor['port'] == port:
                return hypervisor
        return None
        
    def stopProcHypervisors(self):
        """ Shutdown all started hypervisors 
        """
    
        if globals.GApp != None and globals.GApp.systconf['dynamips']:
            self.setDefaults()
        for hypervisor in globals.GApp.dynagen.dynamips.values():
            hypervisor.reset()
        globals.GApp.dynagen.dynamips.clear()
        for hypervisor in self.hypervisors:
            debug("Hypervisor manager: close hypervisor on port " + str(hypervisor['port']))
            hypervisor['proc_instance'].close()
            hypervisor['proc_instance'] = None
        self.hypervisors = []

    def preloadDynamips(self):
        """ Preload Dynamips
        """

        proc = QtCore.QProcess(globals.GApp.mainWindow)
        port = globals.hypervisor_baseport
        
        if self.hypervisor_wd:
            # set the working directory
            proc.setWorkingDirectory(self.hypervisor_wd)
        # start dynamips in hypervisor mode (-H)
        proc.start(self.hypervisor_path,  ['-H', str(port)])
        if proc.waitForStarted() == False:
            return False
            
        # give 5 seconds to the hypervisor to accept connections
        count = 5
        connection_success = False
        for nb in range(count + 1):
            s = socket(AF_INET, SOCK_STREAM)
            s.setblocking(0)
            s.settimeout(300)
            try:
                s.connect(('localhost', port))
            except:
                s.close()
                time.sleep(1)
                continue
            connection_success = True
            break
        if connection_success:
            s.close()
            return True
        return False

    def showHypervisors(self):
        """ Show hypervisors port & load
        """
        
        print "Memory usage limit per hypervisor : " + str(globals.GApp.systconf['dynamips'].memory_limit) + " MB"
        print '%-10s %-10s' % ('Port','Memory load')
        for hypervisor in self.hypervisors:
            print '%-10s %-10s' % (hypervisor['port'], str(hypervisor['load']) + ' MB')
    
