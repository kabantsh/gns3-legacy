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

import os, sys, socket
import GNS3.NETFile as netfile
import GNS3.Dynagen.dynamips_lib as lib
import GNS3.Globals as globals 
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow, QAction, QActionGroup, QAction, QIcon
from GNS3.Ui.Form_MainWindow import Ui_MainWindow
from GNS3.Ui.Form_About import Ui_AboutDialog
from GNS3.IOSDialog import IOSDialog
from GNS3.ProjectDialog import ProjectDialog
from GNS3.Utils import translate, fileBrowser
from GNS3.HypervisorManager import HypervisorManager
from GNS3.Config.Preferences import PreferencesDialog
from GNS3.Config.Config import ConfDB
from GNS3.Node.IOSRouter import IOSRouter
from GNS3.Node.Cloud import Cloud

class Workspace(QMainWindow, Ui_MainWindow):
    """ This class is for managing the whole GUI `Workspace'.
        Currently a Workspace is similar to a MainWindow
    """

    def __init__(self):
        
        # Initialize some variables
        self.projectFile = None
        self.projectWorkdir= None
        self.projectConfigs = None

        # Initialize the windows 
        QMainWindow.__init__(self)
        self.submenu_Docks = QtGui.QMenu()
        Ui_MainWindow.setupUi(self, self)
        self.__createMenus()
        self.__connectActions()
        self.setCorner(QtCore.Qt.TopLeftCorner, QtCore.Qt.LeftDockWidgetArea)
        self.setCorner(QtCore.Qt.BottomLeftCorner, QtCore.Qt.LeftDockWidgetArea)
        self.setCorner(QtCore.Qt.TopRightCorner, QtCore.Qt.RightDockWidgetArea)
        self.setCorner(QtCore.Qt.BottomRightCorner, QtCore.Qt.RightDockWidgetArea)

        # Workspace flags
        self.flg_showHostname = False

    def __connectActions(self):
        """ Connect all needed pair (action, SIGNAL)
        """

        self.connect(self.action_Export, QtCore.SIGNAL('triggered()'), self.__action_Export)
        self.connect(self.action_Add_link, QtCore.SIGNAL('triggered()'), self.__action_addLink)
        self.connect(self.action_IOS_images, QtCore.SIGNAL('triggered()'), self.__action_IOSImages)
        self.connect(self.action_ShowHostnames, QtCore.SIGNAL('triggered()'), self.__action_ShowHostnames)
        self.connect(self.action_ZoomIn, QtCore.SIGNAL('triggered()'), self.__action_ZoomIn)
        self.connect(self.action_ZoomOut, QtCore.SIGNAL('triggered()'), self.__action_ZoomOut)
        self.connect(self.action_ZoomReset, QtCore.SIGNAL('triggered()'), self.__action_ZoomReset)
        self.connect(self.action_SelectAll, QtCore.SIGNAL('triggered()'), self.__action_SelectAll)
        self.connect(self.action_SelectNone, QtCore.SIGNAL('triggered()'), self.__action_SelectNone)
        self.connect(self.action_TelnetAll,  QtCore.SIGNAL('triggered()'), self.__action_TelnetAll)
        self.connect(self.action_StartAll,  QtCore.SIGNAL('triggered()'), self.__action_StartAll)
        self.connect(self.action_StopAll,  QtCore.SIGNAL('triggered()'), self.__action_StopAll)
        self.connect(self.action_SuspendAll,  QtCore.SIGNAL('triggered()'), self.__action_SuspendAll)
        self.connect(self.action_About,  QtCore.SIGNAL('triggered()'), self.__action_About)
        self.connect(self.action_AboutQt,  QtCore.SIGNAL('triggered()'), self.__action_AboutQt)
        self.connect(self.action_New,  QtCore.SIGNAL('triggered()'), self.__action_NewProject)
        self.connect(self.action_Open,  QtCore.SIGNAL('triggered()'), self.__action_OpenFile)
        self.connect(self.action_Save,  QtCore.SIGNAL('triggered()'), self.__action_Save)
        self.connect(self.action_SaveAs,  QtCore.SIGNAL('triggered()'), self.__action_SaveAs)
        self.connect(self.action_Preferences, QtCore.SIGNAL('triggered()'), self.__action_Preferences)
        self.connect(self.action_AddNote, QtCore.SIGNAL('triggered()'), self.__action_AddNote)
        self.connect(self.action_Clear, QtCore.SIGNAL('triggered()'), self.__action_Clear)

    def __createMenus(self):
        """ Add own menu actions, and create new sub-menu
        """

        self.subm = self.submenu_Docks
        self.subm.addAction(self.dockWidget_NodeTypes.toggleViewAction())
        self.subm.addAction(self.dockWidget_TopoSum.toggleViewAction())
        self.subm.addAction(self.dockWidget_Console.toggleViewAction())
        self.menu_View.addSeparator().setText(translate("Workspace", "Docks"))
        self.menu_View.addMenu(self.subm)

    def retranslateUi(self, MainWindow):
    
        Ui_MainWindow.retranslateUi(self, MainWindow)
        self.submenu_Docks.setTitle(translate('Workspace', 'Docks'))

        # Retranslate dock contents...
        try:
            self.nodesDock.retranslateUi(self.nodesDock)
            self.treeWidget_TopologySummary.retranslateUi(self.treeWidget_TopologySummary)
        except Exception,e:
            # Ignore if not implemented
            pass

    def __export(self, name, format):
        """ Export the view to an image
        """

        rect = self.graphicsView.viewport().rect()
        pixmap = QtGui.QPixmap(rect.width(), rect.height())
        pixmap.fill(QtCore.Qt.white)
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView.render(painter)
        painter.end()
        pixmap.save(name, format)

    def __action_Export(self):
        """ Export the scene to an image file
        """
    
        filedialog = QtGui.QFileDialog(self)
        selected = QtCore.QString()
        exports = 'PNG File (*.png);;JPG File (*.jpeg *.jpg);;BMP File (*.bmp);;XPM File (*.xpm *.xbm)'
        path = QtGui.QFileDialog.getSaveFileName(filedialog, 'Export', '.', exports, selected)
        if not path:
            return
        path = unicode(path,  'utf-8')
        if str(selected) == 'PNG File (*.png)' and path[-4:] != '.png':
            path = path + '.png'
        if str(selected) == 'JPG File (*.jpeg *.jpg)' and (path[-4:] != '.jpg' or  path[-5:] != '.jpeg'):
            path = path + '.jpeg'
        if str(selected) == 'BMP File (*.bmp)' and path[-4:] != '.bmp':
            path = path + '.bmp'
        if str(selected) == 'BMP File (*.bmp)' and (path[-4:] != '.xpm' or path[-4:] != '.xbm'):
            path = path + '.xpm'
        try:
            self.__export(path, str(str(selected)[:3]))
        except IOError, (errno, strerror):
            QtGui.QMessageBox.critical(self, 'Open',  u'Open: ' + strerror)

    def clear(self):
        """ Clear all the workspace
        """
        
        globals.GApp.workspace.setWindowTitle("GNS3")
        self.projectFile = None
        self.projectWorkdir = None
        self.projectConfigs = None
        globals.GApp.topology.clear()
        for item in globals.GApp.topology.items():
            globals.GApp.topology.removeItem(item)
            
    def __action_Clear(self):
        """ Clear the topology
        """

        reply = QtGui.QMessageBox.question(self, translate("Workspace", "Message"), translate("Workspace", "Are you sure to clear the topology?"), 
                                            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.clear()
        #TODO: clean files ?
            
    def __action_AddNote(self):
        """ Add a note to the scene
        """

        if not self.action_AddNote.isChecked():
            globals.addingNote = False
            globals.GApp.scene.setCursor(QtCore.Qt.ArrowCursor)
        else:
            globals.addingNote = True
            globals.GApp.scene.setCursor(QtCore.Qt.IBeamCursor)
            
    def __action_addLink(self):
        """ Implement the QAction `addLink'
        - This function manage the creation of a connection between two nodes.
        """

        if not self.action_Add_link.isChecked():
            self.action_Add_link.setText(translate('Workspace', 'Add a link'))
            self.action_Add_link.setIcon(QIcon(':/icons/connection.svg'))
            globals.addingLinkFlag = False
            globals.GApp.scene.cleanFlags()
            globals.GApp.scene.setCursor(QtCore.Qt.ArrowCursor)
        else:
            if not globals.GApp.systconf['general'].manual_connection:
                menu = QtGui.QMenu()
                for linktype in globals.linkTypes.keys():
                    menu.addAction(linktype)
                menu.connect(menu, QtCore.SIGNAL("triggered(QAction *)"), self.__setLinkType)
                menu.exec_(QtGui.QCursor.pos())
            else:
                globals.currentLinkType =  globals.Enum.LinkType.Manual
            
            self.action_Add_link.setText(translate('Workspace', 'Cancel'))
            self.action_Add_link.setIcon(QIcon(':/icons/cancel.svg'))
            globals.addingLinkFlag = True
            globals.GApp.scene.setCursor(QtCore.Qt.CrossCursor)

    def __setLinkType(self,  action):
        """ Set the link type to use
        """

        action = str(action.text())
        globals.currentLinkType = globals.linkTypes[action]

    def __action_IOSImages(self):
        """ Implement the QAction `IOSImages'
        - Show a dialog to configure IOSImages
          - Add / Edit / Delete images
          - Add / Edit / Delete hypervisors
        """

        dialog = IOSDialog()
        dialog.setModal(True)
        dialog.show()
        dialog.exec_()

    def __action_SelectAll(self):
        """ Implement the QAction `SelectAll'
        - Select all node on the topology
        """

        for node in globals.GApp.topology.nodes.itervalues():
            node.setSelected(True)

    def __action_SelectNone(self):
        """ Implement the QAction `SelectNone'
        - Unselect all node on the topology
        """

        for node in globals.GApp.topology.nodes.itervalues():
            node.setSelected(False)

    def __action_ZoomIn(self):
        """ Scale in the scene (QGraphicsView)
        """

        factor_in = pow(2.0, 120 / 240.0)
        globals.GApp.scene.scaleView(factor_in)

    def __action_ZoomOut(self):
        """ Scale out the scene (QGraphicsView)
        """

        factor_out = pow(2.0, -120 / 240.0)
        globals.GApp.scene.scaleView(factor_out)

    def __action_ZoomReset(self):
        """ Restore the default scale on the scene (QGraphicsView)
        """

        globals.GApp.scene.resetMatrix()

    def __action_ShowHostnames(self):
        """ Display/Hide hostnames for all the nodes on the scene
        """
    
        if self.flg_showHostname == False:
            self.flg_showHostname = True
            self.action_ShowHostnames.setText(translate('Workspace', 'Hide hostnames'))
            for node in globals.GApp.topology.nodes.itervalues():
                node.showHostname()
        else:
            self.flg_showHostname = False
            self.action_ShowHostnames.setText(translate('Workspace', 'Show hostnames'))
            for node in globals.GApp.topology.nodes.itervalues():
                node.removeHostname()
        
    def __action_TelnetAll(self):
        """ Telnet to all started IOS routers
        """
    
        for node in globals.GApp.topology.nodes.itervalues():
            if isinstance(node, IOSRouter) and node.get_dynagen_device().state == 'running':
                node.console()

    def __launchProgressDialog(self,  action,  text):
        """ Launch a progress dialog and do a action
            action: string
            text: string
        """
    
        node_list = []
        for node in globals.GApp.topology.nodes.values():
            if isinstance(node, IOSRouter):
                node_list.append(node)
                
        count = len(node_list)
        progress = QtGui.QProgressDialog(text, translate("Workspace", "Abort"), 0, count, globals.GApp.mainWindow)
        progress.setMinimum(1)
        progress.setWindowModality(QtCore.Qt.WindowModal)
        globals.GApp.processEvents(QtCore.QEventLoop.AllEvents)
        current = 0
        for node in node_list:
            progress.setValue(current)
            globals.GApp.processEvents(QtCore.QEventLoop.AllEvents | QtCore.QEventLoop.WaitForMoreEvents, 1000)
            if progress.wasCanceled():
                progress.reset()
                break
            try:
                if action == 'start':
                    node.startNode(progress=True)
                if action == 'stop':
                    node.stopNode(progress=True)
                if action == 'suspend':
                    node.suspendNode(progress=True)
            except lib.DynamipsError, msg:
                QtGui.QMessageBox.critical(self, node.hostname + ': ' + translate("Workspace", "Dynamips error"),  str(msg))
            except lib.DynamipsWarning,  msg:
                QtGui.QMessageBox.warning(self,  node.hostname + ': ' + translate("Workspace", "Dynamips warning"),  str(msg))
                continue
            except (lib.DynamipsErrorHandled,  socket.error):
                QtGui.QMessageBox.critical(self, node.hostname + ': ' + translate("Workspace", "Dynamips error"), translate("Workspace", "Connection lost"))
                progress.reset()
                return
            current += 1
        progress.setValue(count)
        progress.deleteLater()
        progress = None
    
    def __action_StartAll(self):
        """ Start all nodes
        """

        self.__launchProgressDialog('start', translate("Workspace", "Starting nodes ..."))
        
    def __action_StopAll(self):
        """ Stop all nodes
        """
        
        self.__launchProgressDialog('stop', translate("Workspace", "Stopping nodes ..."))

    def __action_SuspendAll(self):
        """ Suspend all nodes
        """
        
        self.__launchProgressDialog('suspend', translate("Workspace", "Suspending nodes ..."))
        
    def __action_About(self):
        """ Show GNS3 about dialog
        """

        dialog = QtGui.QDialog()
        ui = Ui_AboutDialog()
        ui.setupUi(dialog)
        dialog.show()
        dialog.exec_()
    
    def __action_AboutQt(self):
        """ Show Qt about dialog
        """
        
        QtGui.QMessageBox.aboutQt(self)

    def __action_Preferences(self):
        """ Show the preferences dialog
        """

        dialog = PreferencesDialog()
        dialog.show()
        dialog.exec_()

    def __action_ProjectPreferences(self):
        """ Show Project Preferences dialog
        """
        dialog = PreferencesDialog('Project')
    
        dialog.show()
        dialog.exec_()
       
    def load_netfile(self, file):
        """ Load a .net file"""

        if file == None:
            return
            
        path = os.path.abspath(file)
        if not os.path.isfile(path):
            QtGui.QMessageBox.critical(self, translate("Workspace", "Loading"), unicode(translate("Workspace", "Invalid file %s")) % file)
            return
        self.projectFile = path
        self.setWindowTitle("GNS3 - " + self.projectFile)
        net = netfile.NETFile()
        globals.GApp.scene.resetMatrix()
        net.import_net_file(path)
        self.statusbar.showMessage(translate("Workspace", "File loaded..."))
            
    def __action_NewProject(self):
        """ Create a new project
        """

        dialog = ProjectDialog()
        dialog.show()
        if dialog.exec_():
            self.clear()
            globals.GApp.workspace.setWindowTitle("GNS3")
            self.projectWorkdir = None
            self.projectConfigs = None
            (self.projectFile, self.projectWorkdir, self.projectConfigs) = dialog.saveProjectSettings()
            if not self.projectFile:
                QtGui.QMessageBox.critical(self, translate("Workspace", "New Project"),  translate("Workspace", "Can't create a project"))
                return
            try:
                if self.projectWorkdir:
                    os.mkdir(self.projectWorkdir)
                if self.projectConfigs:
                    os.mkdir(self.projectConfigs)
            except OSError, (errno, strerror):
                pass
            self.setWindowTitle("GNS3 Project - " + self.projectFile)
            self.statusbar.showMessage(translate("Workspace", "Project loaded..."))

    def __action_OpenFile(self):
        """ Open a file
        """

        if globals.GApp.systconf['dynamips'].path == '':
            QtGui.QMessageBox.warning(self, translate("Workspace", "Open a file"), translate("Workspace", "The path to Dynamips must be configured"))
            self.__action_Preferences()
            return

        (path, selected) = fileBrowser(translate("Workspace", "Open a file"),  filter = 'NET file (*.net);;All files (*.*)', 
                                       directory=globals.GApp.systconf['general'].project_path).getFile()
        if path != None:
            try:
                if str(selected) == 'NET file (*.net)':
                    # here the loading
                    self.projectWorkdir = None
                    self.projectConfigs = None
                    self.load_netfile(path)
            except IOError, (errno, strerror):
                QtGui.QMessageBox.critical(self, 'Open',  u'Open: ' + strerror)
        
    def __action_Save(self):
        """ Save to a file (scenario or dynagen .NET format)
        """

        if self.projectFile is None:
            return self.__action_SaveAs()

        try:
            net = netfile.NETFile()
            globals.GApp.scene.resetMatrix()
            net.export_net_file(self.projectFile)
            self.statusbar.showMessage(translate("Workspace", "File saved..."))
        except IOError, (errno, strerror):
            QtGui.QMessageBox.critical(self, 'Open',  u'Open: ' + strerror)
        
    def __action_SaveAs(self):
        """ Save as (scenario or dynagen .NET format)
        """

        fb = fileBrowser(translate("Workspace", "Save Project As"), 
                                filter='NET file (*.net);;All files (*.*)', directory=globals.GApp.systconf['general'].project_path)
        (path, selected) = fb.getSaveFile()

        if path != None and path != '':
            if str(selected) == 'NET file (*.net)':
                if path[-4:] != '.net':
                    path = path + '.net'
                self.projectFile = path
                self.setWindowTitle("GNS3 - " + self.projectFile)
                net = netfile.NETFile()
                globals.GApp.scene.resetMatrix()
                net.export_net_file(path)

    def closeEvent(self, event):
        """ Ask to close GNS3
        """
        
        reply = QtGui.QMessageBox.question(self, translate("Workspace", "Message"), translate("Workspace", "Are you sure to quit?"), 
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            globals.GApp.topology.clear()
            event.accept()
        else:
            event.ignore()
