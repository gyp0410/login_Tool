# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(394, 382)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 40, 231, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_stature = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_stature.setObjectName("lineEdit_stature")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_stature)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_weight = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_weight)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_age = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_age)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.btn_calculate = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_calculate.setObjectName("btn_calculate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.btn_calculate)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setEnabled(True)
        self.comboBox.setAccessibleName("")
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_end = QtWidgets.QLabel(Form)
        self.label_end.setGeometry(QtCore.QRect(60, 220, 231, 41))
        self.label_end.setText("")
        self.label_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_end.setObjectName("label_end")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "身高："))
        self.lineEdit_stature.setPlaceholderText(_translate("Form", "单位：m"))
        self.label_2.setText(_translate("Form", "体重："))
        self.lineEdit_weight.setPlaceholderText(_translate("Form", "单位：kg"))
        self.label_3.setText(_translate("Form", "年龄："))
        self.label_4.setText(_translate("Form", "性别："))
        self.btn_calculate.setText(_translate("Form", "计算"))
        self.comboBox.setItemText(0, _translate("Form", "男"))
        self.comboBox.setItemText(1, _translate("Form", "女"))
