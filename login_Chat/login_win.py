from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QMainWindow, QLineEdit
from ui import login, signin, signup
from window import SQL
import sys


class My_UI(QWidget, login.Ui_Form):
    def __init__(self,parent=None):
        #super().setupUi(Form)
        super(My_UI, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        #登录按钮验证密码
        self.btn_login.clicked.connect(self.check)

        #退出程序按钮
        self.btn_cancel.clicked.connect(self.cancel)

        #注册按钮
        self.btn_signin.clicked.connect(self.on_button_signup)

        #显示密码按钮
        self.btn_check.clicked.connect(self.yanma)

        #让密码框先隐藏密码
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def yanma(self):
        if self.btn_check.isChecked():                  #如果显示密码按键按下
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)        #普通模式，显示密码
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)      #密码模式，隐藏密码

    #账号密码检查
    def check(self):
        account = self.lineEdit_id.text()           #account获取lineEdit_id的文本

        count = SQL.Judge_account(account)          #count 获得匹配账号的返回值 1为有账号 2 没有账号
        if count != 1:
            replay = QMessageBox.warning(self, "警告", "账号不存在，请重新输入",
                                         QMessageBox.Retry, QMessageBox.Retry)
            if replay == QMessageBox.Retry:
                self.lineEdit_id.clear()            #lineEdit_id文本清空
                self.lineEdit_password.clear()      #lineEdit_password文本清空
        else:
            password = self.lineEdit_password.text()    #password获得lineEdit_password的文本
            count = SQL.Judge_ac_and_pw(account, password)   #count 获得匹配账号密码的返回值  1 登录成功 2 密码错误
            if count == 1:
                replay = QMessageBox.warning(self, '恭喜', '登录成功',
                                             QMessageBox.Ok, QMessageBox.Ok)
                if replay == QMessageBox.Ok:
                    main.hide()                             #将登录界面隐藏起来，将主界面打开
                    self.main_2 = Sign_In()
                    self.main_2.show()

            else:
                reply = QMessageBox.warning(self, "警告", "密码错误",
                                            QMessageBox.Retry, QMessageBox.Retry)
                if reply == QMessageBox.Retry:
                    self.lineEdit_password.clear()


    def on_button_signup(self):  # 按下“注册账号”的按钮
        main.close()                    #关闭登录界面，打开注册界面
        self.signin = Sign_Up()
        self.signin.show()




    #退出程序
    def cancel(self):
        sys.exit()






class Sign_Up(QWidget, signup.Ui_Form):
    def __init__(self,parent=None):
        super(Sign_Up, self).__init__(parent)
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        self.account_str = "长度为5-15位，由数字和字母组成"
        self.tip_id.setText(self.account_str)
        self.tip_id.setStyleSheet("color:black;")
        self.tip_pw.setText("长度为6-15位，由数字和字母组成")
        self.tip_pw2.setText("再次确认密码")
        self.tip_pw.setStyleSheet("color:black;")
        self.tip_pw2.setStyleSheet("color:black;")

        #注册按钮
        self.sign_up.clicked.connect(self.On_button_signin)

        #退出按钮
        self.new_cancel.clicked.connect(My_UI.cancel)





    def confirm_account(self):
        """判断账号是否为正确格式"""
        self.account_count = 0

        account = self.lineEdit_newid.text()

        if len(account) == 0:
            self.account_str = "账号为空"
        elif len(account) < 2:
            self.account_str = "账号长度低于5位"
        else:
            count = SQL.Judge_account(account)
            if count == 1:
                self.account_str = "账号已存在"

        if self.account_str != "长度为5-15位，由数字和字母组成":
            QMessageBox.warning(self, "警告", self.account_str)
            self.tip_id.setText(self.account_str)
            self.tip_id.setStyleSheet("color:red;")
            self.account_count = 1



    def confirm_password(self):
        """确认密码是否为正确格式"""
        self.password_count = 0

        password = self.lineEdit_newpw.text()
        con_password = self.lineEdit_newpw2.text()
        if len(password) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
            self.tip_pw.setText("密码为空")
            self.tip_pw.setStyleSheet("color:red;")
            self.password_count = 1
        elif len(password) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
            self.tip_pw.setText("密码长度低于6位")
            self.tip_pw.setStyleSheet("color:red;")
            self.password_count = 1
        elif password != con_password:
            reply = QMessageBox.critical(self, '错误', '两次输入的密码不一致',
                                         QMessageBox.Retry, QMessageBox.Retry)
            self.tip_pw2.setText("两次输入的密码不一致")
            self.tip_pw2.setStyleSheet("color:red;")  # 把标签信息修改为红色
            if reply == QMessageBox.Retry:
                self.lineEdit_newpw.clear()
                self.lineEdit_newpw2.clear()
                self.password_count = 1



    def Add_Account(self):
        """注册成功后的操作
            将账号和密码放进数据库"""

        account = self.lineEdit_newid.text()
        password = self.lineEdit_newpw.text()


        cn = SQL.pymssql.connect("DESKTOP-AT2JRG0", "gyp", "gaoyupeng", "test")
        cursor = cn.cursor()

        sql = '''insert into name_account(name,password)
                 values('%s','%s')
              ''' % (account, password)
        cursor.execute(sql)
        cn.commit()





    def On_button_signin(self):
        self.confirm_account()
        if self.account_count == 0:
            self.confirm_password()

        if self.account_count == 0 and self.password_count == 0:
            self.Add_Account()
            replay = QMessageBox.information(self, "恭喜", "注册成功", QMessageBox.Ok, QMessageBox.Ok)
            if replay == QMessageBox.Ok:
                self.sign_up.close()






class Sign_In(QMainWindow, signin.Ui_MainWindow):
    def __init__(self,parent=None):
        super(Sign_In, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = My_UI()
    main.show()
    sys.exit(app.exec_())