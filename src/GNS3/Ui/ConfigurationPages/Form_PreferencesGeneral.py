# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_PreferencesGeneral.ui'
#
# Created: Fri May 25 08:52:52 2012
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PreferencesGeneral(object):
    def setupUi(self, PreferencesGeneral):
        PreferencesGeneral.setObjectName(_fromUtf8("PreferencesGeneral"))
        PreferencesGeneral.resize(539, 544)
        self.vboxlayout = QtGui.QVBoxLayout(PreferencesGeneral)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.tabWidget = QtGui.QTabWidget(PreferencesGeneral)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setEnabled(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.langsBox = QtGui.QComboBox(self.tab)
        self.langsBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.langsBox.sizePolicy().hasHeightForWidth())
        self.langsBox.setSizePolicy(sizePolicy)
        self.langsBox.setObjectName(_fromUtf8("langsBox"))
        self.gridLayout_2.addWidget(self.langsBox, 1, 0, 1, 1)
        self.checkBoxProjectDialog = QtGui.QCheckBox(self.tab)
        self.checkBoxProjectDialog.setChecked(True)
        self.checkBoxProjectDialog.setObjectName(_fromUtf8("checkBoxProjectDialog"))
        self.gridLayout_2.addWidget(self.checkBoxProjectDialog, 2, 0, 1, 1)
        self.checkBoxRelativePaths = QtGui.QCheckBox(self.tab)
        self.checkBoxRelativePaths.setChecked(True)
        self.checkBoxRelativePaths.setObjectName(_fromUtf8("checkBoxRelativePaths"))
        self.gridLayout_2.addWidget(self.checkBoxRelativePaths, 3, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.slowStartAll = QtGui.QSpinBox(self.tab)
        self.slowStartAll.setMaximum(10000)
        self.slowStartAll.setObjectName(_fromUtf8("slowStartAll"))
        self.gridLayout_2.addWidget(self.slowStartAll, 6, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 7, 0, 1, 1)
        self.autoSave = QtGui.QSpinBox(self.tab)
        self.autoSave.setMaximum(10000)
        self.autoSave.setProperty(_fromUtf8("value"), 60)
        self.autoSave.setObjectName(_fromUtf8("autoSave"))
        self.gridLayout_2.addWidget(self.autoSave, 8, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.ProjectPath = QtGui.QLineEdit(self.groupBox_2)
        self.ProjectPath.setObjectName(_fromUtf8("ProjectPath"))
        self.gridlayout.addWidget(self.ProjectPath, 1, 0, 1, 1)
        self.ProjectPath_browser = QtGui.QToolButton(self.groupBox_2)
        self.ProjectPath_browser.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.ProjectPath_browser.setObjectName(_fromUtf8("ProjectPath_browser"))
        self.gridlayout.addWidget(self.ProjectPath_browser, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.IOSPath = QtGui.QLineEdit(self.groupBox_2)
        self.IOSPath.setObjectName(_fromUtf8("IOSPath"))
        self.gridlayout.addWidget(self.IOSPath, 3, 0, 1, 1)
        self.IOSPath_browser = QtGui.QToolButton(self.groupBox_2)
        self.IOSPath_browser.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.IOSPath_browser.setObjectName(_fromUtf8("IOSPath_browser"))
        self.gridlayout.addWidget(self.IOSPath_browser, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 9, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(471, 21, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 0, 1, 1)
        self.checkBoxCheckForUpdate = QtGui.QCheckBox(self.tab)
        self.checkBoxCheckForUpdate.setChecked(True)
        self.checkBoxCheckForUpdate.setObjectName(_fromUtf8("checkBoxCheckForUpdate"))
        self.gridLayout_2.addWidget(self.checkBoxCheckForUpdate, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout = QtGui.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.comboBoxPreconfigTerminalCommands = QtGui.QComboBox(self.tab_3)
        self.comboBoxPreconfigTerminalCommands.setObjectName(_fromUtf8("comboBoxPreconfigTerminalCommands"))
        self.gridLayout.addWidget(self.comboBoxPreconfigTerminalCommands, 1, 0, 1, 1)
        self.pushButtonUseTerminalCommand = QtGui.QPushButton(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonUseTerminalCommand.sizePolicy().hasHeightForWidth())
        self.pushButtonUseTerminalCommand.setSizePolicy(sizePolicy)
        self.pushButtonUseTerminalCommand.setObjectName(_fromUtf8("pushButtonUseTerminalCommand"))
        self.gridLayout.addWidget(self.pushButtonUseTerminalCommand, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEditTermCommand = QtGui.QLineEdit(self.tab_3)
        self.lineEditTermCommand.setObjectName(_fromUtf8("lineEditTermCommand"))
        self.gridLayout.addWidget(self.lineEditTermCommand, 3, 0, 1, 1)
        self.checkBoxUseShell = QtGui.QCheckBox(self.tab_3)
        self.checkBoxUseShell.setChecked(False)
        self.checkBoxUseShell.setObjectName(_fromUtf8("checkBoxUseShell"))
        self.gridLayout.addWidget(self.checkBoxUseShell, 4, 0, 1, 1)
        self.checkBoxBringConsoleToFront = QtGui.QCheckBox(self.tab_3)
        self.checkBoxBringConsoleToFront.setObjectName(_fromUtf8("checkBoxBringConsoleToFront"))
        self.gridLayout.addWidget(self.checkBoxBringConsoleToFront, 5, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 2)
        self.doubleSpinBoxConsoleDelay = QtGui.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBoxConsoleDelay.setDecimals(1)
        self.doubleSpinBoxConsoleDelay.setMinimum(0.0)
        self.doubleSpinBoxConsoleDelay.setSingleStep(0.5)
        self.doubleSpinBoxConsoleDelay.setProperty(_fromUtf8("value"), 1.0)
        self.doubleSpinBoxConsoleDelay.setObjectName(_fromUtf8("doubleSpinBoxConsoleDelay"))
        self.gridLayout.addWidget(self.doubleSpinBoxConsoleDelay, 7, 0, 1, 2)
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 315, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 2)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridlayout1 = QtGui.QGridLayout(self.tab_2)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout1.addWidget(self.label_5, 0, 0, 1, 1)
        self.workspaceWidth = QtGui.QSpinBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workspaceWidth.sizePolicy().hasHeightForWidth())
        self.workspaceWidth.setSizePolicy(sizePolicy)
        self.workspaceWidth.setMinimum(500)
        self.workspaceWidth.setMaximum(1000000)
        self.workspaceWidth.setSingleStep(100)
        self.workspaceWidth.setProperty(_fromUtf8("value"), 2000)
        self.workspaceWidth.setObjectName(_fromUtf8("workspaceWidth"))
        self.gridlayout1.addWidget(self.workspaceWidth, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout1.addWidget(self.label_6, 1, 0, 1, 1)
        self.workspaceHeight = QtGui.QSpinBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workspaceHeight.sizePolicy().hasHeightForWidth())
        self.workspaceHeight.setSizePolicy(sizePolicy)
        self.workspaceHeight.setMinimum(500)
        self.workspaceHeight.setMaximum(1000000)
        self.workspaceHeight.setSingleStep(100)
        self.workspaceHeight.setProperty(_fromUtf8("value"), 1000)
        self.workspaceHeight.setObjectName(_fromUtf8("workspaceHeight"))
        self.gridlayout1.addWidget(self.workspaceHeight, 1, 1, 1, 1)
        self.checkBoxDrawRectangle = QtGui.QCheckBox(self.tab_2)
        self.checkBoxDrawRectangle.setChecked(True)
        self.checkBoxDrawRectangle.setObjectName(_fromUtf8("checkBoxDrawRectangle"))
        self.gridlayout1.addWidget(self.checkBoxDrawRectangle, 2, 0, 1, 2)
        self.checkBoxManualConnections = QtGui.QCheckBox(self.tab_2)
        self.checkBoxManualConnections.setChecked(True)
        self.checkBoxManualConnections.setObjectName(_fromUtf8("checkBoxManualConnections"))
        self.gridlayout1.addWidget(self.checkBoxManualConnections, 3, 0, 1, 2)
        self.checkBoxShowStatusPoints = QtGui.QCheckBox(self.tab_2)
        self.checkBoxShowStatusPoints.setChecked(True)
        self.checkBoxShowStatusPoints.setObjectName(_fromUtf8("checkBoxShowStatusPoints"))
        self.gridlayout1.addWidget(self.checkBoxShowStatusPoints, 4, 0, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(20, 251, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem2, 5, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 499, 63))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self._2 = QtGui.QHBoxLayout(self.groupBox_3)
        self._2.setObjectName(_fromUtf8("_2"))
        self.labelConfigurationPath = QtGui.QLabel(self.groupBox_3)
        self.labelConfigurationPath.setObjectName(_fromUtf8("labelConfigurationPath"))
        self._2.addWidget(self.labelConfigurationPath)
        spacerItem3 = QtGui.QSpacerItem(16, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self._2.addItem(spacerItem3)
        self.pushButton_ClearConfiguration = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_ClearConfiguration.setObjectName(_fromUtf8("pushButton_ClearConfiguration"))
        self._2.addWidget(self.pushButton_ClearConfiguration)
        self.Button_export_configuration = QtGui.QPushButton(self.tab_4)
        self.Button_export_configuration.setGeometry(QtCore.QRect(30, 130, 191, 31))
        self.Button_export_configuration.setObjectName(_fromUtf8("Button_export_configuration"))
        self.Button_import_configuration = QtGui.QPushButton(self.tab_4)
        self.Button_import_configuration.setGeometry(QtCore.QRect(30, 180, 191, 31))
        self.Button_import_configuration.setObjectName(_fromUtf8("Button_import_configuration"))
        self.label_12 = QtGui.QLabel(self.tab_4)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(240, 170, 221, 41))
        self.label_12.setFrameShadow(QtGui.QFrame.Raised)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(240, 200, 221, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(240, 220, 221, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(240, 240, 191, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.vboxlayout.addWidget(self.tabWidget)

        self.retranslateUi(PreferencesGeneral)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreferencesGeneral)

    def retranslateUi(self, PreferencesGeneral):
        PreferencesGeneral.setWindowTitle(QtGui.QApplication.translate("PreferencesGeneral", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PreferencesGeneral", "Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxProjectDialog.setText(QtGui.QApplication.translate("PreferencesGeneral", "Launch the project dialog at startup", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxRelativePaths.setText(QtGui.QApplication.translate("PreferencesGeneral", "Use relative path for projects", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PreferencesGeneral", "Delay between each device start when starting all devices:", None, QtGui.QApplication.UnicodeUTF8))
        self.slowStartAll.setSuffix(QtGui.QApplication.translate("PreferencesGeneral", " seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("PreferencesGeneral", "Autosave:", None, QtGui.QApplication.UnicodeUTF8))
        self.autoSave.setSuffix(QtGui.QApplication.translate("PreferencesGeneral", " seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("PreferencesGeneral", "Paths", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PreferencesGeneral", "Project directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.ProjectPath_browser.setText(QtGui.QApplication.translate("PreferencesGeneral", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PreferencesGeneral", "OS image (IOS, Qemu, PIX etc.) directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.IOSPath_browser.setText(QtGui.QApplication.translate("PreferencesGeneral", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCheckForUpdate.setText(QtGui.QApplication.translate("PreferencesGeneral", "Automatically check for update", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("PreferencesGeneral", "General Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("PreferencesGeneral", "Preconfigurated terminal commands:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUseTerminalCommand.setText(QtGui.QApplication.translate("PreferencesGeneral", "&Use", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PreferencesGeneral", "Terminal command:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxUseShell.setText(QtGui.QApplication.translate("PreferencesGeneral", "Launch this command using the system default shell", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxBringConsoleToFront.setToolTip(QtGui.QApplication.translate("PreferencesGeneral", "<html>This option will attempt to bring existing opened console window to front, instead of opening a new window.<br>If no existing opened console window exists, it will start a new  console window.</html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxBringConsoleToFront.setText(QtGui.QApplication.translate("PreferencesGeneral", "Bring console window to front (experimental feature)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("PreferencesGeneral", "Delay between each console when consoling to all devices:", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleSpinBoxConsoleDelay.setSuffix(QtGui.QApplication.translate("PreferencesGeneral", " seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("PreferencesGeneral", "Terminal command magic strings:\n"
"%h = device server \n"
"%p = device port\n"
"%d = device hostname", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("PreferencesGeneral", "Terminal Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PreferencesGeneral", "Workspace width:", None, QtGui.QApplication.UnicodeUTF8))
        self.workspaceWidth.setSuffix(QtGui.QApplication.translate("PreferencesGeneral", " px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PreferencesGeneral", "Workspace height:", None, QtGui.QApplication.UnicodeUTF8))
        self.workspaceHeight.setSuffix(QtGui.QApplication.translate("PreferencesGeneral", " px", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxDrawRectangle.setText(QtGui.QApplication.translate("PreferencesGeneral", "Draw a rectangle when an item is selected", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxManualConnections.setText(QtGui.QApplication.translate("PreferencesGeneral", "Always use manual mode when adding links", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowStatusPoints.setText(QtGui.QApplication.translate("PreferencesGeneral", "Show link status points on the workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("PreferencesGeneral", "GUI Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("PreferencesGeneral", "Configuration file", None, QtGui.QApplication.UnicodeUTF8))
        self.labelConfigurationPath.setText(QtGui.QApplication.translate("PreferencesGeneral", "Unknown location", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ClearConfiguration.setText(QtGui.QApplication.translate("PreferencesGeneral", "&Clear it", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_export_configuration.setText(QtGui.QApplication.translate("PreferencesGeneral", "export configuration file", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_import_configuration.setText(QtGui.QApplication.translate("PreferencesGeneral", "import configuration file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("PreferencesGeneral", "your configuration file will be backup ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("PreferencesGeneral", "next to gns3.ini. any previous backup ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("PreferencesGeneral", "will be overwrite", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("PreferencesGeneral", "gns3 will restart", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("PreferencesGeneral", "Configuration File", None, QtGui.QApplication.UnicodeUTF8))

