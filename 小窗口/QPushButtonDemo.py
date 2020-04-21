'''

按钮控件 (QPushuButton)

QAbstractButton

QPushButton
AToolButton
QRadioButton
QCheckBox


'''


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtCore import *
import webbrowser
url = 'http://www.baidu.com'


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()

        self.button1 = QPushButton('第1个按钮')
        self.button1.setText('Fist Button1')
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(self.buttonState)
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))
        layout.addWidget(self.button1)



        #在文本前面显示图像

        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./images/py.ico')))
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))
        layout.addWidget(self.button2)


        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.button5 = QPushButton('百度一下，你就知道')
        self.button5.clicked.connect(self.openURL)
        layout.addWidget(self.button5)


        self.setLayout(layout)
        self.resize(400, 300)
    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() + '>')

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')


    def openURL(self):
        if self.button5.clicked:
            webbrowser.open_new_tab(url)










if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
