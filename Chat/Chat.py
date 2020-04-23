

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.setGeometry(300, 300, 500, 247)
        #登陆窗口无边界
        self.setWindowFlag(Qt.FramelessWindowHint)
        #登陆窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        #定义多个空label
        self.label_null1 = QLabel()
        self.label_null2 = QLabel()
        self.label_null3 = QLabel()
        self.label_null4 = QLabel()
        self.label_new = QLabel()
        #定义创建新账户标签并设置信号槽绑定事件
        self.label_new.setText("<a href ='#' >注册新用户</a>")
        self.label_new.setStyle('''color: rgb(253,129,53);''')
        self.label_new.linkActivated.connect(self.idnew)
        #设置隐藏密码RadioButton
        self.btn_check = QRadioButton("显示密码")
        #self.btn_check.setStyleSheet('''color: rgb(253,129,53)''')
        self.btn_check.clicked.connect(self.yanma)
        #登陆与退出按钮，设置按钮颜色及事件绑定
        self.btn_login = QPushButton("登录")
        self.btn_cancel = QPushButton("退出")
        #self.btn_login.setStyleSheet('''color: white;
                #        backgrround-color: rgb(218,181,150);''')
        #self.btn_cancel.setStyleSheet('''color: white;
                 #       backgrround-color: rgb(218,181,150);''')
        self.btn_login.clicked.connect(self.check)
        self.btn_cancel.clicked.connect(self.cancel)
        #账号和密码
        self.lineEdit_id = QLineEdit()
        self.lineEdit_id.setPlaceholderText("账号")
        self.lintEdit_password = QLineEdit()
        self.lintEdit_password.setPlaceholderText("密码")
        #布局设置
        layout = QHBoxLayout()
        wid_login_right = QWidget()
        wid_login_left = QLabel()
        g = QGridLayout()
        g.addWidget(self.lineEdit_id, 1, 1, 1, 2)
        g.addWidget(self.lintEdit_password, 2, 1, 1, 2)
        g.addWidget(self.btn_check, 3, 1)
        g.addWidget(self.btn_login, 4, 1)
        g.addWidget(self.btn_cancel, 4, 3)
        g.addWidget(self.label_null1, 5, 1)
        g.addWidget(self.label_null2, 6, 1)
        g.addWidget(self.label_null3, 7, 1)
        g.addWidget(self.label_null4, 8, 1)
        g.addWidget(self.label_new, 9, 2)
        wid_login_left.setLayout(g)
        layout.addWidget(wid_login_left)
        layout.addWidget(wid_login_right)
        self.setLayout(layout)

    #密码隐藏
    def yanma(self):
        if self.btn_check.isChecked():
            self.lintEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lintEdit_password.setEchoMode(QLineEdit.Password)

    #登录时核查账号及密码是否正确
    def check(self):
        temp = False
        self.id_password = {}
        id = open("账号.txt")
        password = open("密码.txt")
        i = 0
        for line1 in id:
            m = i+1
            for line2 in password:
                i = i+1
                if i == m:
                    self.id_password[line1]=line2
                    break
                if i < m:
                    continue
                    #如果输入账号不在账号表文件中，则推送消息框提示
        if self.lineEdit_id.text()+"\n" not in self.id_password:
            replay = QMessageBox.warning(self, "!", "账号或者密码输入错误", QMessageBox.Yes)
        else:
            if self.id_password[self.lineEdit_id.text()+"\n"] == self.lintEdit_password.text()+"\n":
                #账号密码验证成功，创建主界面，进入信息管理程序，并关闭登陆窗口
                self.shop = QWidget()
                self.shop.show()
                self.close()
            else:
                replay = QMessageBox.warning(self, "!", "账号或密码输入错误", QMessageBox.Yes)
        id.close()
        password.close()
        #创建新的账号
    def idnew(self):
        self.label_idnew_id = QLabel("账号")
        self.label_idnew_password = QLabel("密码")
        self.lineEdit_idnew_id = QLineEdit()
        self.lineEdit_idnew_password = QLineEdit()
        self.btn_idnew_confirm = QPushButton("注册")
        self.btn_idnew_confirm.clicked.connect(self.idnewConfirm)
        self.btn_idnew_cancel = QPushButton("取消")
        self.btn_idnew_cancel.clicked.connect(self.idnewClose)
        self.idnew =  QWidget()
        layout_idnew = QGridLayout()
        layout_idnew.addWidget(self.label_idnew_id, 1, 0)
        layout_idnew.addWidget(self.label_idnew_password, 2 , 0)
        layout_idnew.addWidget(self.lineEdit_id, 1, 1, 1, 2)
        layout_idnew.addWidget(self.lintEdit_password, 2, 1, 1, 2)
        layout_idnew.addWidget(self.btn_idnew_confirm, 3, 1)
        layout_idnew.addWidget(self.btn_idnew_cancel, 3, 2)
        self.idnew.setLayout(layout_idnew)
        self.idnew.move(self.pos())
        self.idnew.resize(200, 133)
        self.idnew.setWindowFlag(Qt.FramelessWindowHint)
        self.paintEngine(self)
        #self.idnew.setStyleSheet("background-color :rgb(253,216,174)")
        self.idnew.show()
        #新账号注册的确认
    def idnewConfirm(self):
        id = open("账号.txt", "r+")
        password  = open("密码.txt", "r+")
        self.id_password = {}
        i = 0
        for line1 in id:
            m = i+1
            for lien2 in password:
                i = i+1
                if i == m:
                    self.id_password[line1] = lien2
                    break
                if i < m:
                    continue
        if self.lineEdit_idnew_id.text() == "":
            replay = QMessageBox.warning(self, "!", "账号不准为空", QMessageBox.Yes)
        else:
            if self.lineEdit_idnew_id.text() + "\n" in self.id_password:
                replay = QMessageBox.warning(self, "!", "账号已存在", QMessageBox.Yes)
            else:
                if self.lineEdit_idnew_password.text() == "":
                    replay = QMessageBox.warning(self, "!", "密码不准为空", QMessageBox.Yes)
                else:
                    id.write(self.lineEdit_idnew_id.text() + "\n")
                    password.write(self.lineEdit_idnew_password.text() + "\n")
                    replay = QMessageBox.warning(self, "!", "注册成功！", QMessageBox.Yes)
                    self.idnew.close()
        id.close()
        password.close()
    #添加背景图片
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("123.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    # 关闭创新账号窗口
    def idnewClose(self):
        self.idnew.close()

    # 取消创建新账号，并退出创建窗口
    def cancel(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = Login()
    d.show()
    sys.exit(app.exec())