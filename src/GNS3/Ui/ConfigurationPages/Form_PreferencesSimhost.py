# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_PreferencesSimhost.ui'
#
# Created: Sun Dec  7 02:50:47 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PreferencesSimhost(object):
    def setupUi(self, PreferencesSimhost):
        PreferencesSimhost.setObjectName("PreferencesSimhost")
        PreferencesSimhost.resize(QtCore.QSize(QtCore.QRect(0,0,430,439).size()).expandedTo(PreferencesSimhost.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(PreferencesSimhost)
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtGui.QTabWidget(PreferencesSimhost)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName("tab_1")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab_1)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.groupBox = QtGui.QGroupBox(self.tab_1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")

        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName("gridlayout")

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,2)

        self.simhost_path = QtGui.QLineEdit(self.groupBox)
        self.simhost_path.setObjectName("simhost_path")
        self.gridlayout.addWidget(self.simhost_path,1,0,1,2)

        self.simhost_path_browser = QtGui.QToolButton(self.groupBox)
        self.simhost_path_browser.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.simhost_path_browser.setObjectName("simhost_path_browser")
        self.gridlayout.addWidget(self.simhost_path_browser,1,2,1,1)

        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,2,0,1,2)

        self.simhost_workdir = QtGui.QLineEdit(self.groupBox)
        self.simhost_workdir.setObjectName("simhost_workdir")
        self.gridlayout.addWidget(self.simhost_workdir,3,0,1,2)

        self.simhost_workdir_browser = QtGui.QToolButton(self.groupBox)
        self.simhost_workdir_browser.setObjectName("simhost_workdir_browser")
        self.gridlayout.addWidget(self.simhost_workdir_browser,3,2,1,1)

        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,4,0,1,1)

        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6,4,1,1,1)

        self.simhost_basePort = QtGui.QSpinBox(self.groupBox)
        self.simhost_basePort.setMaximum(65535)
        self.simhost_basePort.setProperty("value",QtCore.QVariant(9000))
        self.simhost_basePort.setObjectName("simhost_basePort")
        self.gridlayout.addWidget(self.simhost_basePort,5,0,1,1)

        self.simhost_baseUDP = QtGui.QSpinBox(self.groupBox)
        self.simhost_baseUDP.setMaximum(65535)
        self.simhost_baseUDP.setProperty("value",QtCore.QVariant(35000))
        self.simhost_baseUDP.setObjectName("simhost_baseUDP")
        self.gridlayout.addWidget(self.simhost_baseUDP,5,1,1,1)
        self.vboxlayout1.addWidget(self.groupBox)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.pushButtonTestSimhost = QtGui.QPushButton(self.tab_1)
        self.pushButtonTestSimhost.setObjectName("pushButtonTestSimhost")
        self.hboxlayout.addWidget(self.pushButtonTestSimhost)

        self.labelDynamipsStatus = QtGui.QLabel(self.tab_1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDynamipsStatus.sizePolicy().hasHeightForWidth())
        self.labelDynamipsStatus.setSizePolicy(sizePolicy)
        self.labelDynamipsStatus.setObjectName("labelDynamipsStatus")
        self.hboxlayout.addWidget(self.labelDynamipsStatus)
        self.vboxlayout1.addLayout(self.hboxlayout)

        spacerItem = QtGui.QSpacerItem(390,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_1,"")
        self.vboxlayout.addWidget(self.tabWidget)

        self.retranslateUi(PreferencesSimhost)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PreferencesSimhost)

    def retranslateUi(self, PreferencesSimhost):
        PreferencesSimhost.setWindowTitle(QtGui.QApplication.translate("PreferencesSimhost", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("PreferencesSimhost", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PreferencesSimhost", "Executable path:", None, QtGui.QApplication.UnicodeUTF8))
        self.simhost_path_browser.setText(QtGui.QApplication.translate("PreferencesSimhost", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PreferencesSimhost", "Working directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.simhost_workdir_browser.setText(QtGui.QApplication.translate("PreferencesSimhost", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PreferencesSimhost", "Base port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PreferencesSimhost", " Base UDP:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonTestSimhost.setText(QtGui.QApplication.translate("PreferencesSimhost", "&Test", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QtGui.QApplication.translate("PreferencesSimhost", "Simhost hypervisor", None, QtGui.QApplication.UnicodeUTF8))

