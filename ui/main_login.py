# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color:#808080")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.teacher = QtWidgets.QPushButton(self.centralwidget)
        self.teacher.setGeometry(QtCore.QRect(350, 300, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.teacher.setFont(font)
        self.teacher.setStyleSheet("background-color:#ffffff")
        self.teacher.setObjectName("teacher")
        self.student = QtWidgets.QPushButton(self.centralwidget)
        self.student.setGeometry(QtCore.QRect(350, 400, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.student.setFont(font)
        self.student.setStyleSheet("background-color:#ffffff")
        self.student.setObjectName("student")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(150, 140, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet("background-color:#ffffff")
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.teacher.setText(_translate("MainWindow", "Teacher"))
        self.student.setText(_translate("MainWindow", "Student"))
        self.welcome.setText(_translate("MainWindow", "WELCOME TO SCHOOL MANAGEMENT SYSTEM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
