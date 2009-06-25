# -*- coding: utf-8 -*-
# vim: expandtab ts=4 sw=4 sts=4:
#
# Copyright (C) 2007-2008 GNS3 Dev Team
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

import os, re, shutil
import GNS3.Dynagen.dynagen as dynagen
import GNS3.Dynagen.dynagen as dynagen_namespace
import GNS3.Globals as globals
import GNS3.Dynagen.dynamips_lib as lib
import GNS3.Dynagen.pemu_lib as pix
import GNS3.Telnet as console
from PyQt4 import QtCore, QtGui
from GNS3.Node.AbstractNode import AbstractNode
from GNS3.Defaults.AnyEmuDefaults import AnyEmuDefaults, FWDefaults, ASADefaults
from GNS3.Utils import translate, debug, error

emu_id = 1

def init_emu_id(id = 1):
    global emu_id
    emu_id = id

class AnyEmuDevice(AbstractNode, AnyEmuDefaults):
    """ AnyEmuDevice class implementing a Emulated devices
    """

    model = 'AbstractAnyEmuDevice'
    
    def __init__(self, renderer_normal, renderer_select):

        AbstractNode.__init__(self, renderer_normal, renderer_select)
        AnyEmuDefaults.__init__(self)

        # assign a new hostname
        global emu_id
        
        # check if hostname has already been assigned
        for node in globals.GApp.topology.nodes.itervalues():
            if self.basehostname + str(emu_id) == node.hostname:
                emu_id = emu_id + 1
                break
        
        self.hostname = self.basehostname + str(emu_id)
        emu_id = emu_id + 1
        AbstractNode.setCustomToolTip(self)

        self.dynagen = globals.GApp.dynagen
        self.local_config = None
        self.f = '%s %s' %(self.basehostname, self.hostname)
        self.running_config = None
        self.defaults_config = None
        self.emudev = None

        self.emudev_options = [
            'ram',
            'image'
            ]

    def __del__(self):

        self.delete_emudev()

    def delete_emudev(self):
        """ Delete this emulated device
        """
        if self.emudev:
            try:
                self.stopNode()
                del self.dynagen.devices[self.hostname]
                if self.emudev in self.pemu.devices:
                    self.pemu.devices.remove(self.emudev)
                self.dynagen.update_running_config()
            except:
                pass
            self.emudev = None

    def set_hostname(self, hostname):
        """ Set a hostname
        """

        self.hostname = hostname
        self.f = '%s %s' % (self.basehostname, self.hostname)
        self.updateToolTips()

    def setCustomToolTip(self):
        """ Set a custom tool tip
        """

        if self.emudev:
            self.setToolTip(self.emudev.info())
        else:
            AbstractNode.setCustomToolTip(self)
        
    def get_running_config_name(self):
        """ Return node name as stored in the running config
        """

        return (self.f)

    def create_config(self):
        """ Creates the configuration of this firewall
        """

        assert(self.emudev)
        self.local_config = {}
        for option in self.emudev_options:
            try:
                self.local_config[option] = getattr(self.emudev, option)
            except AttributeError:
                continue
        return self.local_config

    def get_config(self):
        """ Returns the local configuration copy
        """

        assert(self.emudev)
        return self.local_config
        
    def duplicate_config(self):
        """ Returns a copy of the local configuration
        """

        return self.local_config.copy()

    def set_config(self, config):
        """ Set a configuration in Pemu
            config: dict
        """

        assert(self.emudev)
        # apply the options
        for option in self.emudev_options:
            try:
                emu_option = getattr(self.emudev, option)
            except AttributeError:
                continue
            if emu_option != config[option]:
                try:
                    setattr(self.emudev, option, config[option])
                except lib.DynamipsError, e:
                    error(e)

        self.local_config = config.copy()
        self.dynagen.update_running_config()
        self.running_config =  self.dynagen.running_config[self.d][self.f]
        debug("Node " + self.hostname + ": running config: " + str(self.running_config))
        globals.GApp.topology.changed = True
        self.setCustomToolTip()

    def getInterfaces(self):
        """ Return all interfaces
        """

        # 5 ethernet interfaces per default
        return (['e0', 'e1', 'e2', 'e3', 'e4'])

    def get_dynagen_device(self):
        """ Returns the dynagen device corresponding to this bridge
        """

        assert(self.emudev)
        return (self.emudev)

    def set_dynagen_device(self, emudev):
        """ Set a dynagen device in this node, used for .net import
        """

        model = self.model
        self.emudev = emudev
        self.running_config = self.dynagen.running_config[self.d][self.f]
        self.defaults_config = self.dynagen.defaults_config[self.d][model]
        self.create_config()

    def reconfigNode(self, new_hostname):
        """ Used when changing the hostname
        """

        links = self.getEdgeList()
        if len(links):
            QtGui.QMessageBox.critical(globals.GApp.mainWindow, translate("AnyEmuDevice", "New hostname"),
                                       translate("AnyEmuDevice", "Cannot rename a connected emulated device because qemuwrapper does not support removal"))
            return
        self.delete_emudev()
        if self.hostname != new_hostname:
            try:
                pemu_name = self.pemu.host + ':10525'
                shutil.move(self.dynagen.dynamips[pemu_name].workingdir + os.sep + self.hostname, self.dynagen.dynamips[pemu_name].workingdir + os.sep + new_hostname)
            except:
                debug("Cannot move emulator's working directory")
        self.set_hostname(new_hostname)
        try:
            self.create_emudev()
        except lib.DynamipsError, msg:
            QtGui.QMessageBox.critical(globals.GApp.mainWindow, translate("AnyEmuDevice", "Dynamips error"),  unicode(msg))
            self.delete_emudev()
            globals.GApp.topology.deleteNode(self.id)
            return
        self.set_config(self.local_config)

    def configNode(self):
        """ Node configuration
        """

        self.create_emudev()
        self.create_config()
        return True

    def get_devdefaults(self):
        """ Get device defaults
        """

        model = self.model
        devdefaults = {}
        for key in dynagen_namespace.DEVICETUPLE:
            devdefaults[key] = {}

        config = globals.GApp.dynagen.defaults_config
        #go through all section under dynamips server in running config and populate the devdefaults with model defaults
        for f in config[self.d]:
            firewall_model = config[self.d][f]

            # compare whether this is defaults section
            if firewall_model.name in dynagen_namespace.DEVICETUPLE and firewall_model.name == model:
                # Populate the appropriate dictionary
                for scalar in firewall_model.scalars:
                    if firewall_model[scalar] != None:
                        devdefaults[firewall_model.name][scalar] = firewall_model[scalar]

        #check whether a defaults section for this router type exists
        if model in dynagen_namespace.DEVICETUPLE:
            if devdefaults[model] == {} and not devdefaults[model].has_key('image'):
                error('Create a defaults section for ' + model + ' first! Minimum setting is image name')
                return False
            elif not devdefaults[model].has_key('image'):
                error('Specify image name for ' + model + ' routers first!')
                return False
        else:
            error('Bad model: ' + model)
            return False
        return devdefaults

    def create_emudev(self):

        model = self.model
        self.dynagen.update_running_config()
        devdefaults = self.get_devdefaults()
        if devdefaults == False:
            return False
        pemu_name = self.pemu.host + ':10525'
        self.emudev = self._make_devinstance(pemu_name)
        self.dynagen.setdefaults(self.emudev, devdefaults[model])
        self.dynagen.devices[self.hostname] = self.emudev
        debug('%s %s created' % (self.friendly_name, self.emudev.name))

        self.dynagen.update_running_config()
        self.running_config = self.dynagen.running_config[self.d][self.f]
        self.defaults_config = self.dynagen.defaults_config[self.d][model]
        self.setCustomToolTip()

    def startNode(self, progress=False):
        """ Start the node
        """

        if not self.emudev.image:
            print unicode(translate(self.basehostname, "%s: no device image")) % self.hostname
            return
        try:
            if self.emudev.state == 'stopped':
                self.emudev.start()
        except:
            if progress:
                raise
            else:
                return

        self.startupInterfaces()
        self.state = 'running'
        globals.GApp.mainWindow.treeWidget_TopologySummary.changeNodeStatus(self.hostname, 'running')

    def stopNode(self, progress=False):
        """ Stop this node
        """

        if self.emudev.state != 'stopped':
            try:
                self.emudev.stop()
            except:
                if progress:
                    raise

            self.shutdownInterfaces()
            self.state = self.emudev.state
            globals.GApp.mainWindow.treeWidget_TopologySummary.changeNodeStatus(self.hostname, self.emudev.state)

    def suspendNode(self, progress=False):
        """ Suspend this node
        """

        pass

    def console(self):
        """ Start a telnet console and connect it to this router
        """

        if self.emudev and self.emudev.state == 'running' and self.emudev.console:
            console.connect(self.emudev.dynamips.host, self.emudev.console, self.hostname)

    def mousePressEvent(self, event):
        """ Call when the node is clicked
            event: QtGui.QGraphicsSceneMouseEvent instance
        """

        AbstractNode.mousePressEvent(self, event)

class FW(AnyEmuDevice, FWDefaults):
    instance_counter = 0
    model = '525'
    basehostname = 'FW'
    friendly_name = 'Firewall'
    
    def __init__(self, *args, **kwargs):
        AnyEmuDevice.__init__(self, *args, **kwargs)
        FWDefaults.__init__(self)
        self.emudev_options.extend([
            'key',
            'serial',
            ])
        
    def _make_devinstance(self, pemu_name):
        from GNS3.Dynagen import pemu_lib
        return pemu_lib.FW(self.dynagen.dynamips[pemu_name], self.hostname)

class ASA(AnyEmuDevice, ASADefaults):
    instance_counter = 0
    model = '5520'
    basehostname = 'ASA'
    friendly_name ='ASAFirewall'
    
    def __init__(self, *args, **kwargs):
        AnyEmuDevice.__init__(self, *args, **kwargs)
        ASADefaults.__init__(self)
        debug('Hello, I have initialized and my model is %s' % self.model)
    
    def _make_devinstance(self, pemu_name):
        from GNS3.Dynagen import pemu_lib
        return pemu_lib.ASA(self.dynagen.dynamips[pemu_name], self.hostname)

class Olive(AnyEmuDevice, ASADefaults):

    instance_counter = 0
    model = 'O-series'
    basehostname = 'OLIVE'
    friendly_name ='OliveRouter'

    def __init__(self, *args, **kwargs):
        AnyEmuDevice.__init__(self, *args, **kwargs)
        ASADefaults.__init__(self)
        debug('Hello, I have initialized and my model is %s' % self.model)

    def _make_devinstance(self, pemu_name):
        from GNS3.Dynagen import pemu_lib
        return pemu_lib.Olive(self.dynagen.dynamips[pemu_name], self.hostname)