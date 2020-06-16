# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(551, 453)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 60, 411, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_newid = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_newid.setObjectName("lineEdit_newid")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_newid)
        self.tip_id = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tip_id.setFont(font)
        self.tip_id.setText("")
        self.tip_id.setObjectName("tip_id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tip_id)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_newpw = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_newpw.setObjectName("lineEdit_newpw")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_newpw)
        self.tip_pw = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tip_pw.setFont(font)
        self.tip_pw.setText("")
        self.tip_pw.setObjectName("tip_pw")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tip_pw)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_newpw2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_newpw2.setObjectName("lineEdit_newpw2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_newpw2)
        self.tip_pw2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tip_pw2.setFont(font)
        self.tip_pw2.setText("")
        self.tip_pw2.setObjectName("tip_pw2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.tip_pw2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 250, 331, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sign_up = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sign_up.setObjectName("sign_up")
        self.horizontalLayout.addWidget(self.sign_up)
        self.new_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.new_cancel.setObjectName("new_cancel")
        self.horizontalLayout.addWidget(self.new_cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "账号："))
        self.label_3.setText(_translate("Form", "密码："))
        self.label_5.setText(_translate("Form", "确认密码："))
        self.sign_up.setText(_translate("Form", "注册"))
        self.new_cancel.setText(_translate("Form", "退出"))
