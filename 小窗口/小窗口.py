# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '小窗口.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 0, 1, 1, 1)
        self.sort_Button = QtWidgets.QPushButton(self.centralwidget)
        self.sort_Button.setObjectName("sort_Button")
        self.gridLayout.addWidget(self.sort_Button, 1, 1, 1, 1)
        self.random_Button = QtWidgets.QPushButton(self.centralwidget)
        self.random_Button.setObjectName("random_Button")
        self.gridLayout.addWidget(self.random_Button, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 26))
        self.menubar.setObjectName("menubar")
        self.menunew = QtWidgets.QMenu(self.menubar)
        self.menunew.setObjectName("menunew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menunew.addAction(self.actionNew)
        self.menunew.addSeparator()
        self.menunew.addAction(self.actionOpen)
        self.menunew.addSeparator()
        self.menunew.addAction(self.actionSave)
        self.menunew.addSeparator()
        self.menubar.addAction(self.menunew.menuAction())
        self.toolBar.addAction(self.actionNew)

        self.retranslateUi(MainWindow)
        #self.random_Button.clicked.connect(MainWindow.random_number)
        #self.sort_Button.clicked.connect(MainWindow.sort_number)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sort_Button.setText(_translate("MainWindow", "产生"))
        self.random_Button.setText(_translate("MainWindow", "随机"))
        self.label.setText(_translate("MainWindow", "为产生的随机数排序"))
        self.menunew.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "创建新文件"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+A"))
