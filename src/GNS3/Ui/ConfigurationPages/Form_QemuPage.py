# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_QemuPage.ui'
#
# Created: Tue Jun  1 20:57:05 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_QemuPage(object):
    def setupUi(self, QemuPage):
        QemuPage.setObjectName("QemuPage")
        QemuPage.resize(419, 453)
        self.gridLayout = QtGui.QGridLayout(QemuPage)
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtGui.QLabel(QemuPage)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.lineEditImage = QtGui.QLineEdit(QemuPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditImage.sizePolicy().hasHeightForWidth())
        self.lineEditImage.setSizePolicy(sizePolicy)
        self.lineEditImage.setObjectName("lineEditImage")
        self.gridLayout.addWidget(self.lineEditImage, 0, 1, 1, 1)
        self.pushButtonImageBrowser = QtGui.QPushButton(QemuPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonImageBrowser.sizePolicy().hasHeightForWidth())
        self.pushButtonImageBrowser.setSizePolicy(sizePolicy)
        self.pushButtonImageBrowser.setMaximumSize(QtCore.QSize(31, 27))
        self.pushButtonImageBrowser.setObjectName("pushButtonImageBrowser")
        self.gridLayout.addWidget(self.pushButtonImageBrowser, 0, 2, 1, 1)
        self.label_24 = QtGui.QLabel(QemuPage)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 1, 0, 1, 1)
        self.spinBoxRamSize = QtGui.QSpinBox(QemuPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRamSize.sizePolicy().hasHeightForWidth())
        self.spinBoxRamSize.setSizePolicy(sizePolicy)
        self.spinBoxRamSize.setMaximum(100000)
        self.spinBoxRamSize.setSingleStep(4)
        self.spinBoxRamSize.setProperty("value", 96)
        self.spinBoxRamSize.setObjectName("spinBoxRamSize")
        self.gridLayout.addWidget(self.spinBoxRamSize, 1, 1, 1, 2)
        self.label_26 = QtGui.QLabel(QemuPage)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 2, 0, 1, 1)
        self.comboBoxNIC = QtGui.QComboBox(QemuPage)
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
        self.gridLayout.addWidget(self.comboBoxNIC, 2, 1, 1, 2)
        self.label_8 = QtGui.QLabel(QemuPage)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.lineEditOptions = QtGui.QLineEdit(QemuPage)
        self.lineEditOptions.setEnabled(True)
        self.lineEditOptions.setObjectName("lineEditOptions")
        self.gridLayout.addWidget(self.lineEditOptions, 3, 1, 1, 2)
        self.checkBoxKqemu = QtGui.QCheckBox(QemuPage)
        self.checkBoxKqemu.setEnabled(True)
        self.checkBoxKqemu.setObjectName("checkBoxKqemu")
        self.gridLayout.addWidget(self.checkBoxKqemu, 4, 0, 1, 1)
        self.checkBoxKVM = QtGui.QCheckBox(QemuPage)
        self.checkBoxKVM.setEnabled(True)
        self.checkBoxKVM.setObjectName("checkBoxKVM")
        self.gridLayout.addWidget(self.checkBoxKVM, 5, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 281, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)

        self.retranslateUi(QemuPage)
        self.comboBoxNIC.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(QemuPage)

    def retranslateUi(self, QemuPage):
        QemuPage.setWindowTitle(QtGui.QApplication.translate("QemuPage", "Firewall configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("QemuPage", "Qemu Image:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonImageBrowser.setText(QtGui.QApplication.translate("QemuPage", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("QemuPage", "RAM size:", None, QtGui.QApplication.UnicodeUTF8))
        self.spinBoxRamSize.setSuffix(QtGui.QApplication.translate("QemuPage", " MB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("QemuPage", "NIC:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(0, QtGui.QApplication.translate("QemuPage", "ne2k_pci", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(1, QtGui.QApplication.translate("QemuPage", "i82551", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(2, QtGui.QApplication.translate("QemuPage", "i82557b", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(3, QtGui.QApplication.translate("QemuPage", "i82559er", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(4, QtGui.QApplication.translate("QemuPage", "rtl8139", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(5, QtGui.QApplication.translate("QemuPage", "e1000", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(6, QtGui.QApplication.translate("QemuPage", "pcnet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxNIC.setItemText(7, QtGui.QApplication.translate("QemuPage", "virtio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("QemuPage", "Qemu Options:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxKqemu.setText(QtGui.QApplication.translate("QemuPage", "Use KQemu", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxKVM.setText(QtGui.QApplication.translate("QemuPage", "Use KVM (Linux only)", None, QtGui.QApplication.UnicodeUTF8))

