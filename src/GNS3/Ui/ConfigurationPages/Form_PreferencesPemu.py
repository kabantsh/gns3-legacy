# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_PreferencesPemu.ui'
#
# Created: Wed Mar  5 14:28:30 2008
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PreferencesPemu(object):
    def setupUi(self, PreferencesPemu):
        PreferencesPemu.setObjectName("PreferencesPemu")
        PreferencesPemu.resize(QtCore.QSize(QtCore.QRect(0,0,425,436).size()).expandedTo(PreferencesPemu.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(PreferencesPemu)
        self.vboxlayout.setObjectName("vboxlayout")

        self.groupBox_2 = QtGui.QGroupBox(PreferencesPemu)
        self.groupBox_2.setObjectName("groupBox_2")

        self.gridlayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout.setObjectName("gridlayout")

        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,0,0,1,3)

        self.lineEditPemuwrapperPath = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditPemuwrapperPath.setObjectName("lineEditPemuwrapperPath")
        self.gridlayout.addWidget(self.lineEditPemuwrapperPath,1,0,1,2)

        self.PemuwrapperPath_browser = QtGui.QToolButton(self.groupBox_2)
        self.PemuwrapperPath_browser.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.PemuwrapperPath_browser.setObjectName("PemuwrapperPath_browser")
        self.gridlayout.addWidget(self.PemuwrapperPath_browser,1,2,1,1)

        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,2,0,1,2)

        self.lineEditPemuwrapperWorkdir = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditPemuwrapperWorkdir.setObjectName("lineEditPemuwrapperWorkdir")
        self.gridlayout.addWidget(self.lineEditPemuwrapperWorkdir,3,0,1,2)

        self.PemuwrapperWorkdir_browser = QtGui.QToolButton(self.groupBox_2)
        self.PemuwrapperWorkdir_browser.setObjectName("PemuwrapperWorkdir_browser")
        self.gridlayout.addWidget(self.PemuwrapperWorkdir_browser,3,2,1,1)

        self.checkBoxEnablePemuManager = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxEnablePemuManager.setChecked(True)
        self.checkBoxEnablePemuManager.setObjectName("checkBoxEnablePemuManager")
        self.gridlayout.addWidget(self.checkBoxEnablePemuManager,4,0,1,3)

        self.checkBoxPemuManagerImport = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxPemuManagerImport.setChecked(True)
        self.checkBoxPemuManagerImport.setObjectName("checkBoxPemuManagerImport")
        self.gridlayout.addWidget(self.checkBoxPemuManagerImport,5,0,1,3)

        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,6,0,1,1)

        self.lineEditHostExternalPemu = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditHostExternalPemu.setObjectName("lineEditHostExternalPemu")
        self.gridlayout.addWidget(self.lineEditHostExternalPemu,6,1,1,2)
        self.vboxlayout.addWidget(self.groupBox_2)

        self.groupBox = QtGui.QGroupBox(PreferencesPemu)
        self.groupBox.setObjectName("groupBox")

        self.gridlayout1 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.gridlayout1.addWidget(self.label,0,0,1,1)

        self.PixImage = QtGui.QLineEdit(self.groupBox)
        self.PixImage.setObjectName("PixImage")
        self.gridlayout1.addWidget(self.PixImage,0,1,1,1)

        self.PixImage_Browser = QtGui.QToolButton(self.groupBox)
        self.PixImage_Browser.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.PixImage_Browser.setObjectName("PixImage_Browser")
        self.gridlayout1.addWidget(self.PixImage_Browser,0,2,1,1)

        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridlayout1.addWidget(self.label_20,1,0,1,1)

        self.lineEditKey = QtGui.QLineEdit(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditKey.sizePolicy().hasHeightForWidth())
        self.lineEditKey.setSizePolicy(sizePolicy)
        self.lineEditKey.setObjectName("lineEditKey")
        self.gridlayout1.addWidget(self.lineEditKey,1,1,1,2)

        self.label_21 = QtGui.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridlayout1.addWidget(self.label_21,2,0,1,1)

        self.lineEditSerial = QtGui.QLineEdit(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSerial.sizePolicy().hasHeightForWidth())
        self.lineEditSerial.setSizePolicy(sizePolicy)
        self.lineEditSerial.setObjectName("lineEditSerial")
        self.gridlayout1.addWidget(self.lineEditSerial,2,1,1,2)
        self.vboxlayout.addWidget(self.groupBox)

        spacerItem = QtGui.QSpacerItem(20,51,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem)

        self.retranslateUi(PreferencesPemu)
        QtCore.QMetaObject.connectSlotsByName(PreferencesPemu)

    def retranslateUi(self, PreferencesPemu):
        PreferencesPemu.setWindowTitle(QtGui.QApplication.translate("PreferencesPemu", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("PreferencesPemu", "Pemuwrapper", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PreferencesPemu", "Path (pemuwrapper.exe on Windows else pemuwrapper.py):", None, QtGui.QApplication.UnicodeUTF8))
        self.PemuwrapperPath_browser.setText(QtGui.QApplication.translate("PreferencesPemu", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PreferencesPemu", "Working directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.PemuwrapperWorkdir_browser.setText(QtGui.QApplication.translate("PreferencesPemu", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxEnablePemuManager.setText(QtGui.QApplication.translate("PreferencesPemu", "Enable Pemu Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxPemuManagerImport.setText(QtGui.QApplication.translate("PreferencesPemu", "Use Pemu Manager when importing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PreferencesPemu", "Host for an external pemuwrapper:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("PreferencesPemu", "Defaults PIX settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PreferencesPemu", "PIX image:", None, QtGui.QApplication.UnicodeUTF8))
        self.PixImage_Browser.setText(QtGui.QApplication.translate("PreferencesPemu", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("PreferencesPemu", "Key:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("PreferencesPemu", "Serial:", None, QtGui.QApplication.UnicodeUTF8))
