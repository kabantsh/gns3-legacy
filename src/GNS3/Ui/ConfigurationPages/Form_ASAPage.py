# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_ASAPage.ui'
#
# Created: Wed Feb 24 14:29:08 2010
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ASAPage(object):
    def setupUi(self, ASAPage):
        ASAPage.setObjectName("ASAPage")
        ASAPage.resize(419, 453)
        self.gridLayout = QtGui.QGridLayout(ASAPage)
        self.gridLayout.setObjectName("gridLayout")
        self.label_24 = QtGui.QLabel(ASAPage)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)
        self.spinBoxRamSize = QtGui.QSpinBox(ASAPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRamSize.sizePolicy().hasHeightForWidth())
        self.spinBoxRamSize.setSizePolicy(sizePolicy)
        self.spinBoxRamSize.setMaximum(100000)
        self.spinBoxRamSize.setSingleStep(4)
        self.spinBoxRamSize.setProperty("value", 256)
        self.spinBoxRamSize.setObjectName("spinBoxRamSize")
        self.gridLayout.addWidget(self.spinBoxRamSize, 0, 1, 1, 2)
        self.label_26 = QtGui.QLabel(ASAPage)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 0, 1, 1)
        self.comboBoxNIC = QtGui.QComboBox(ASAPage)
        self.comboBoxNIC.setEnabled(True)
        self.comboBoxNIC.setObjectName("comboBoxNIC")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.comboBoxNIC.addItem("")
        self.gridLayout.addWidget(self.comboBoxNIC, 1, 1, 1, 2)
        self.label_8 = QtGui.QLabel(ASAPage)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEditOptions = QtGui.QLineEdit(ASAPage)
        self.lineEditOptions.setEnabled(True)
        self.lineEditOptions.setObjectName("lineEditOptions")
        self.gridLayout.addWidget(self.lineEditOptions, 2, 1, 1, 2)
        self.checkBoxKqemu = QtGui.QCheckBox(ASAPage)
        self.checkBoxKqemu.setEnabled(True)
        self.checkBoxKqemu.setObjectName("checkBoxKqemu")
        self.gridLayout.addWidget(self.checkBoxKqemu, 3, 0, 1, 1)
        self.checkBoxKVM = QtGui.QCheckBox(ASAPage)
        self.checkBoxKVM.setEnabled(True)
        self.checkBoxKVM.setObjectName("checkBoxKVM")
        self.gridLayout.addWidget(self.checkBoxKVM, 3, 1, 1, 1)
        self.label_20 = QtGui.QLabel(ASAPage)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 4, 0, 1, 1)
        self.lineEditInitrd = QtGui.QLineEdit(ASAPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditInitrd.sizePolicy().hasHeightForWidth())
        self.lineEditInitrd.setSizePolicy(sizePolicy)
        self.lineEditInitrd.setObjectName("lineEditInitrd")
        self.gridLayout.addWidget(self.lineEditInitrd, 4, 1, 1, 1)
        self.pushButtonInitrdBrowser = QtGui.QPushButton(ASAPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonInitrdBrowser.sizePolicy().hasHeightForWidth())
        self.pushButtonInitrdBrowser.setSizePolicy(sizePolicy)
        self.pushButtonInitrdBrowser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonInitrdBrowser.setObjectName("pushButtonInitrdBrowser")
        self.gridLayout.addWidget(self.pushButtonInitrdBrowser, 4, 2, 1, 1)
        self.label_21 = QtGui.QLabel(ASAPage)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 5, 0, 1, 1)
        self.lineEditKernel = QtGui.QLineEdit(ASAPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditKernel.sizePolicy().hasHeightForWidth())
        self.lineEditKernel.setSizePolicy(sizePolicy)
        self.lineEditKernel.setObjectName("lineEditKernel")
        self.gridLayout.addWidget(self.lineEditKernel, 5, 1, 1, 1)
        self.pushButtonKernelBrowser = QtGui.QPushButton(ASAPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKernelBrowser.sizePolicy().hasHeightForWidth())
        self.pushButtonKernelBrowser.setSizePolicy(sizePolicy)
        self.pushButtonKernelBrowser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonKernelBrowser.setObjectName("pushButtonKernelBrowser")
        self.gridLayout.addWidget(self.pushButtonKernelBrowser, 5, 2, 1, 1)
        self.label_13 = QtGui.QLabel(ASAPage)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        self.lineEditKernelCmdLine = QtGui.QLineEdit(ASAPage)
        self.lineEditKernelCmdLine.setObjectName("lineEditKernelCmdLine")
        self.gridLayout.addWidget(self.lineEditKernelCmdLine, 6, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 281, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 3)

        self.retranslateUi(ASAPage)
        self.comboBoxNIC.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(ASAPage)

    def retranslateUi(self, ASAPage):
        ASAPage.setWindowTitle(QtGui.QApplication.translate("ASAPage", "Firewall configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("ASAPage", "RAM size:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxRamSize.setSuffix(QtGui.QApplication.translate("ASAPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("ASAPage", "NIC:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(0, QtGui.QApplication.translate("ASAPage", "ne2k_pci", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(1, QtGui.QApplication.translate("ASAPage", "i82551", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(2, QtGui.QApplication.translate("ASAPage", "i82557b", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(3, QtGui.QApplication.translate("ASAPage", "i82559er", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(4, QtGui.QApplication.translate("ASAPage", "rtl8139", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(5, QtGui.QApplication.translate("ASAPage", "e1000", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(6, QtGui.QApplication.translate("ASAPage", "pcnet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(7, QtGui.QApplication.translate("ASAPage", "virtio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ASAPage", "Qemu Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxKqemu.setText(QtGui.QApplication.translate("ASAPage", "Use KQemu", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxKVM.setText(QtGui.QApplication.translate("ASAPage", "UseKVM (Linux only)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("ASAPage", "Initrd:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonInitrdBrowser.setText(QtGui.QApplication.translate("ASAPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("ASAPage", "Kernel:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonKernelBrowser.setText(QtGui.QApplication.translate("ASAPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ASAPage", "Kernel cmd line:", None, QtGui.QApplication.UnicodeUTF8))

