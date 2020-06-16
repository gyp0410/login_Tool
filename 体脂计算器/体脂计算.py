from PyQt5.QtWidgets import QApplication,QMessageBox,QWidget
import sys
from win import Ui_Form
from PyQt5 import QtWidgets
import math
import pymssql


class My_Ui(QWidget,Ui_Form):
    def __init__(self, Form):
        super().setupUi(Form)
        super(My_Ui, self).__init__()
        self.initUI()


    def initUI(self):
        self.btn_calculate.clicked.connect(self.Result)

    def Calculation(self):
        self.falg = False
        if self.lineEdit_stature.text() != '':
            if  self.lineEdit_weight.text() != '':
                if  self.lineEdit_age.text() != '':
                    self.stature = float(self.lineEdit_stature.text())
                    self.weight = float(self.lineEdit_weight.text())
                    self.age = int(self.lineEdit_age.text())
                    self.sex = self.comboBox.currentText()
                    if self.sex == "男":
                        sex_1 = 1
                    elif self.sex == "女":
                        sex_1 = 0
                    BMI = float(self.weight/math.pow(self.stature,2))
                    self.result = 1.2 * BMI + 0.23 * self.age - 5.4 - 10.8 * sex_1
                    print("%.2f，%.1f，%d，%.2f，%d" % (self.stature,self.weight,self.age,BMI,sex_1))
                    self.flag = True
                else:
                    replay = QMessageBox.warning(self, "警告", "年龄不能为空", QMessageBox.Yes | QMessageBox.Yes, QMessageBox.Yes)
            else:
                replay = QMessageBox.warning(self, "警告", "体重不能为空", QMessageBox.Yes | QMessageBox.Yes, QMessageBox.Yes)
        else:
            replay = QMessageBox.warning(self,"警告","身高不能为空",QMessageBox.Yes | QMessageBox.Yes, QMessageBox.Yes)

    def SqlServer(self):
        cn = pymssql.connect("DESKTOP-AT2JRG0", "gyp", "gaoyupeng", "test")
        cursor = cn.cursor()
        stature = self.stature
        weight = self.weight
        age = self.age
        sex = self.sex
        sql = '''insert into information(stature,
                 weights,age,sex,body_fat)
                 values('%.2f','%.1f','%d','%s','%.1f')
               ''' % (stature,weight,age,sex,self.result)
        cursor.execute(sql)
        cn.commit()
        cn.close()

    def Result(self):
        self.Calculation()
        try:
            if  self.flag == True:
                self.SqlServer()
                self.label_end.setText("体脂：%.1f" % self.result)
        except:
                replay = QMessageBox.warning(self,"警告","不能为空",QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    main = My_Ui(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())



