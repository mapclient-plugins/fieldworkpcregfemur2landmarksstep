# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(418, 391)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.label_2 = QLabel(self.configGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEditFHC = QLineEdit(self.configGroupBox)
        self.lineEditFHC.setObjectName(u"lineEditFHC")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditFHC)

        self.label_3 = QLabel(self.configGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEditMEC = QLineEdit(self.configGroupBox)
        self.lineEditMEC.setObjectName(u"lineEditMEC")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditMEC)

        self.label_4 = QLabel(self.configGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEditLEC = QLineEdit(self.configGroupBox)
        self.lineEditLEC.setObjectName(u"lineEditLEC")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditLEC)

        self.label_5 = QLabel(self.configGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.lineEditFGT = QLineEdit(self.configGroupBox)
        self.lineEditFGT.setObjectName(u"lineEditFGT")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEditFGT)

        self.label_7 = QLabel(self.configGroupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.checkBoxGUI = QCheckBox(self.configGroupBox)
        self.checkBoxGUI.setObjectName(u"checkBoxGUI")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.checkBoxGUI)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ConfigureDialog", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("Dialog", u"identifier:  ", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Femoral Head Centre:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Medial Epicondyle:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Lateral Epicondyle:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Greater Trochanter:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"GUI:", None))
        self.checkBoxGUI.setText("")
    # retranslateUi

