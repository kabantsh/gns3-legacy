# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigurationPages/Form_PreferencesGeneral.ui'
#
# Created: Sun Jun  9 18:19:41 2013
#      by: PyQt4 UI code generator 4.8.6
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
        PreferencesGeneral.resize(539, 588)
        PreferencesGeneral.setWindowTitle(QtGui.QApplication.translate("PreferencesGeneral", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_5 = QtGui.QGridLayout(PreferencesGeneral)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tabWidget = QtGui.QTabWidget(PreferencesGeneral)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setEnabled(True)
        self.label.setText(QtGui.QApplication.translate("PreferencesGeneral", "Language:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.langsBox = QtGui.QComboBox(self.tab)
        self.langsBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.langsBox.sizePolicy().hasHeightForWidth())
        self.langsBox.setSizePolicy(sizePolicy)
        self.langsBox.setObjectName(_fromUtf8("langsBox"))
        self.gridLayout_3.addWidget(self.langsBox, 1, 0, 1, 1)
        self.checkBoxProjectDialog = QtGui.QCheckBox(self.tab)
        self.checkBoxProjectDialog.setText(QtGui.QApplication.translate("PreferencesGeneral", "Launch the project dialog at startup", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxProjectDialog.setChecked(True)
        self.checkBoxProjectDialog.setObjectName(_fromUtf8("checkBoxProjectDialog"))
        self.gridLayout_3.addWidget(self.checkBoxProjectDialog, 2, 0, 1, 1)
        self.checkBoxRelativePaths = QtGui.QCheckBox(self.tab)
        self.checkBoxRelativePaths.setText(QtGui.QApplication.translate("PreferencesGeneral", "Use relative path for projects", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxRelativePaths.setChecked(True)
        self.checkBoxRelativePaths.setObjectName(_fromUtf8("checkBoxRelativePaths"))
        self.gridLayout_3.addWidget(self.checkBoxRelativePaths, 3, 0, 1, 1)
        self.checkBoxCheckForUpdate = QtGui.QCheckBox(self.tab)
        self.checkBoxCheckForUpdate.setText(QtGui.QApplication.translate("PreferencesGeneral", "Automatically check for update", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCheckForUpdate.setChecked(True)
        self.checkBoxCheckForUpdate.setObjectName(_fromUtf8("checkBoxCheckForUpdate"))
        self.gridLayout_3.addWidget(self.checkBoxCheckForUpdate, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setText(QtGui.QApplication.translate("PreferencesGeneral", "Delay between each device start when starting all devices:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)
        self.slowStartAll = QtGui.QSpinBox(self.tab)
        self.slowStartAll.setSuffix(QtGui.QApplication.translate("PreferencesGeneral", " seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.slowStartAll.setMaximum(10000)
        self.slowStartAll.setObjectName(_fromUtf8("slowStartAll"))
        self.gridLayout_3.addWidget(self.slowStartAll, 7, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setText(QtGui.QApplication.translate("PreferencesGeneral", "Autosave:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 8, 0, 1, 1)
        self.autoSave = QtGui.QSpinBox(self.tab)
        self.autoSave.setSuffix(QtGui.QApplication.translate("PreferencesGeneral", " seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.autoSave.setMaximum(10000)
        self.autoSave.setProperty("value", 60)
        self.autoSave.setObjectName(_fromUtf8("autoSave"))
        self.gridLayout_3.addWidget(self.autoSave, 9, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("PreferencesGeneral", "Paths", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setText(QtGui.QApplication.translate("PreferencesGeneral", "Project directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.ProjectPath = QtGui.QLineEdit(self.groupBox_2)
        self.ProjectPath.setObjectName(_fromUtf8("ProjectPath"))
        self.gridLayout_4.addWidget(self.ProjectPath, 1, 0, 1, 1)
        self.ProjectPath_browser = QtGui.QToolButton(self.groupBox_2)
        self.ProjectPath_browser.setText(QtGui.QApplication.translate("PreferencesGeneral", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.ProjectPath_browser.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.ProjectPath_browser.setObjectName(_fromUtf8("ProjectPath_browser"))
        self.gridLayout_4.addWidget(self.ProjectPath_browser, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setText(QtGui.QApplication.translate("PreferencesGeneral", "OS image (IOS, Qemu, PIX etc.) directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.IOSPath = QtGui.QLineEdit(self.groupBox_2)
        self.IOSPath.setObjectName(_fromUtf8("IOSPath"))
        self.gridLayout_4.addWidget(self.IOSPath, 3, 0, 1, 1)
        self.IOSPath_browser = QtGui.QToolButton(self.groupBox_2)
        self.IOSPath_browser.setText(QtGui.QApplication.translate("PreferencesGeneral", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.IOSPath_browser.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.IOSPath_browser.setObjectName(_fromUtf8("IOSPath_browser"))
        self.gridLayout_4.addWidget(self.IOSPath_browser, 3, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 10, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("PreferencesGeneral", "Configuration file", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelConfigurationPath = QtGui.QLabel(self.groupBox_3)
        self.labelConfigurationPath.setText(QtGui.QApplication.translate("PreferencesGeneral", "Unknown location", None, QtGui.QApplication.UnicodeUTF8))
        self.labelConfigurationPath.setObjectName(_fromUtf8("labelConfigurationPath"))
        self.gridLayout_2.addWidget(self.labelConfigurationPath, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(16, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 3)
        self.pushButton_ImportConfiguration = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_ImportConfiguration.setText(QtGui.QApplication.translate("PreferencesGeneral", "&Import", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ImportConfiguration.setObjectName(_fromUtf8("pushButton_ImportConfiguration"))
        self.gridLayout_2.addWidget(self.pushButton_ImportConfiguration, 1, 0, 1, 1)
        self.pushButton_ExportConfiguration = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_ExportConfiguration.setText(QtGui.QApplication.translate("PreferencesGeneral", "&Export", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ExportConfiguration.setObjectName(_fromUtf8("pushButton_ExportConfiguration"))
        self.gridLayout_2.addWidget(self.pushButton_ExportConfiguration, 1, 1, 1, 2)
        self.pushButton_ClearConfiguration = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_ClearConfiguration.setText(QtGui.QApplication.translate("PreferencesGeneral", "&Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ClearConfiguration.setObjectName(_fromUtf8("pushButton_ClearConfiguration"))
        self.gridLayout_2.addWidget(self.pushButton_ClearConfiguration, 1, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(186, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 4, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 11, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(471, 21, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 12, 0, 1, 1)
        self.checkBoxAutoScreenshot = QtGui.QCheckBox(self.tab)
        self.checkBoxAutoScreenshot.setText(QtGui.QApplication.translate("PreferencesGeneral", "Include a screenshot when saving a project", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxAutoScreenshot.setChecked(True)
        self.checkBoxAutoScreenshot.setObjectName(_fromUtf8("checkBoxAutoScreenshot"))
        self.gridLayout_3.addWidget(self.checkBoxAutoScreenshot, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout = QtGui.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setText(QtGui.QApplication.translate("PreferencesGeneral", "Preconfigurated terminal commands:", None, QtGui.QApplication.UnicodeUTF8))
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
        self.pushButtonUseTerminalCommand.setText(QtGui.QApplication.translate("PreferencesGeneral", "&Use", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUseTerminalCommand.setObjectName(_fromUtf8("pushButtonUseTerminalCommand"))
        self.gridLayout.addWidget(self.pushButtonUseTerminalCommand, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setText(QtGui.QApplication.translate("PreferencesGeneral", "Terminal command:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEditTermCommand = QtGui.QLineEdit(self.tab_3)
        self.lineEditTermCommand.setObjectName(_fromUtf8("lineEditTermCommand"))
        self.gridLayout.addWidget(self.lineEditTermCommand, 3, 0, 1, 2)
        self.checkBoxUseShell = QtGui.QCheckBox(self.tab_3)
        self.checkBoxUseShell.setText(QtGui.QApplication.translate("PreferencesGeneral", "Launch terminals using the system default shell", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxUseShell.setChecked(False)
        self.checkBoxUseShell.setObjectName(_fromUtf8("checkBoxUseShell"))
        self.gridLayout.addWidget(self.checkBoxUseShell, 7, 0, 1, 1)
        self.checkBoxBringConsoleToFront = QtGui.QCheckBox(self.tab_3)
        self.checkBoxBringConsoleToFront.setToolTip(QtGui.QApplication.translate("PreferencesGeneral", "<html>This option will attempt to bring existing opened console window to front, instead of opening a new window.<br>If no existing opened console window exists, it will start a new  console window.</html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxBringConsoleToFront.setText(QtGui.QApplication.translate("PreferencesGeneral", "Bring console window to front (experimental feature)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxBringConsoleToFront.setObjectName(_fromUtf8("checkBoxBringConsoleToFront"))
        self.gridLayout.addWidget(self.checkBoxBringConsoleToFront, 8, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setText(QtGui.QApplication.translate("PreferencesGeneral", "Delay between each console when consoling to all devices:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.doubleSpinBoxConsoleDelay = QtGui.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBoxConsoleDelay.setSuffix(QtGui.QApplication.translate("PreferencesGeneral", " seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleSpinBoxConsoleDelay.setDecimals(1)
        self.doubleSpinBoxConsoleDelay.setMinimum(0.0)
        self.doubleSpinBoxConsoleDelay.setSingleStep(0.5)
        self.doubleSpinBoxConsoleDelay.setProperty("value", 1.0)
        self.doubleSpinBoxConsoleDelay.setObjectName(_fromUtf8("doubleSpinBoxConsoleDelay"))
        self.gridLayout.addWidget(self.doubleSpinBoxConsoleDelay, 10, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setText(QtGui.QApplication.translate("PreferencesGeneral", "Terminal command magic strings:\n"
"%h = device server \n"
"%p = device port\n"
"%d = device hostname\n"
"%s = device pipe", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 13, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 315, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 14, 0, 1, 2)
        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setText(QtGui.QApplication.translate("PreferencesGeneral", "Terminal command for VirtualBox local console/serial connections:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 2)
        self.lineEditTermCommandVBoxConsole = QtGui.QLineEdit(self.tab_3)
        self.lineEditTermCommandVBoxConsole.setObjectName(_fromUtf8("lineEditTermCommandVBoxConsole"))
        self.gridLayout.addWidget(self.lineEditTermCommandVBoxConsole, 5, 0, 1, 2)
        self.checkBoxCloseTermPrograms = QtGui.QCheckBox(self.tab_3)
        self.checkBoxCloseTermPrograms.setText(QtGui.QApplication.translate("PreferencesGeneral", "Close associated terminal programs when deleting a node", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCloseTermPrograms.setObjectName(_fromUtf8("checkBoxCloseTermPrograms"))
        self.gridLayout.addWidget(self.checkBoxCloseTermPrograms, 6, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setText(QtGui.QApplication.translate("PreferencesGeneral", "Workspace width:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)
        self.workspaceWidth = QtGui.QSpinBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workspaceWidth.sizePolicy().hasHeightForWidth())
        self.workspaceWidth.setSizePolicy(sizePolicy)
        self.workspaceWidth.setSuffix(QtGui.QApplication.translate("PreferencesGeneral", " px", None, QtGui.QApplication.UnicodeUTF8))
        self.workspaceWidth.setMinimum(500)
        self.workspaceWidth.setMaximum(1000000)
        self.workspaceWidth.setSingleStep(100)
        self.workspaceWidth.setProperty("value", 2000)
        self.workspaceWidth.setObjectName(_fromUtf8("workspaceWidth"))
        self.gridLayout_6.addWidget(self.workspaceWidth, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setText(QtGui.QApplication.translate("PreferencesGeneral", "Workspace height:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)
        self.workspaceHeight = QtGui.QSpinBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workspaceHeight.sizePolicy().hasHeightForWidth())
        self.workspaceHeight.setSizePolicy(sizePolicy)
        self.workspaceHeight.setSuffix(QtGui.QApplication.translate("PreferencesGeneral", " px", None, QtGui.QApplication.UnicodeUTF8))
        self.workspaceHeight.setMinimum(500)
        self.workspaceHeight.setMaximum(1000000)
        self.workspaceHeight.setSingleStep(100)
        self.workspaceHeight.setProperty("value", 1000)
        self.workspaceHeight.setObjectName(_fromUtf8("workspaceHeight"))
        self.gridLayout_6.addWidget(self.workspaceHeight, 1, 1, 1, 1)
        self.checkBoxDrawRectangle = QtGui.QCheckBox(self.tab_2)
        self.checkBoxDrawRectangle.setText(QtGui.QApplication.translate("PreferencesGeneral", "Draw a rectangle when an item is selected", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxDrawRectangle.setChecked(True)
        self.checkBoxDrawRectangle.setObjectName(_fromUtf8("checkBoxDrawRectangle"))
        self.gridLayout_6.addWidget(self.checkBoxDrawRectangle, 2, 0, 1, 2)
        self.checkBoxManualConnections = QtGui.QCheckBox(self.tab_2)
        self.checkBoxManualConnections.setText(QtGui.QApplication.translate("PreferencesGeneral", "Always use manual mode when adding links", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxManualConnections.setChecked(True)
        self.checkBoxManualConnections.setObjectName(_fromUtf8("checkBoxManualConnections"))
        self.gridLayout_6.addWidget(self.checkBoxManualConnections, 3, 0, 1, 2)
        self.checkBoxShowStatusPoints = QtGui.QCheckBox(self.tab_2)
        self.checkBoxShowStatusPoints.setText(QtGui.QApplication.translate("PreferencesGeneral", "Show link status points on the workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxShowStatusPoints.setChecked(True)
        self.checkBoxShowStatusPoints.setObjectName(_fromUtf8("checkBoxShowStatusPoints"))
        self.gridLayout_6.addWidget(self.checkBoxShowStatusPoints, 4, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(20, 251, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem4, 5, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(PreferencesGeneral)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreferencesGeneral)

    def retranslateUi(self, PreferencesGeneral):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("PreferencesGeneral", "General Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("PreferencesGeneral", "Terminal Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("PreferencesGeneral", "GUI Settings", None, QtGui.QApplication.UnicodeUTF8))

