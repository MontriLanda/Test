# Form implementation generated from reading ui file 'toyo.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_toyo(object):
    def setupUi(self, toyo):
        toyo.setObjectName("toyo")
        toyo.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=toyo)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_emp_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_emp_name.setGeometry(QtCore.QRect(30, 50, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(36)
        self.lbl_emp_name.setFont(font)
        self.lbl_emp_name.setObjectName("lbl_emp_name")
        self.lbl_position = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_position.setGeometry(QtCore.QRect(40, 140, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(36)
        self.lbl_position.setFont(font)
        self.lbl_position.setObjectName("lbl_position")
        self.lbl_salary = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_salary.setGeometry(QtCore.QRect(40, 220, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(36)
        self.lbl_salary.setFont(font)
        self.lbl_salary.setObjectName("lbl_salary")
        self.txt_emp_name = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.txt_emp_name.setGeometry(QtCore.QRect(240, 50, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(24)
        self.txt_emp_name.setFont(font)
        self.txt_emp_name.setObjectName("txt_emp_name")
        self.txt_position = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.txt_position.setGeometry(QtCore.QRect(240, 140, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(26)
        self.txt_position.setFont(font)
        self.txt_position.setObjectName("txt_position")
        self.txt_salary = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.txt_salary.setGeometry(QtCore.QRect(240, 220, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(24)
        self.txt_salary.setFont(font)
        self.txt_salary.setObjectName("txt_salary")
        self.btnAdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(320, 310, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(26)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(self.AddEmp) # Conno
        toyo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=toyo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        toyo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=toyo)
        self.statusbar.setObjectName("statusbar")
        toyo.setStatusBar(self.statusbar)

        self.retranslateUi(toyo)
        QtCore.QMetaObject.connectSlotsByName(toyo)

    def retranslateUi(self, toyo):
        _translate = QtCore.QCoreApplication.translate
        toyo.setWindowTitle(_translate("toyo", "โปรแกรมเพิ่มข้อมูลพนังงาน"))
        self.lbl_emp_name.setText(_translate("toyo", "ชื่อพนักงาน"))
        self.lbl_position.setText(_translate("toyo", "ตำแหน่ง"))
        self.lbl_salary.setText(_translate("toyo", "เงินเดือน"))
        self.btnAdd.setText(_translate("toyo", "เพิ่มข้อมูล"))
      
        
    def AddEmp (self):
        conn = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'toyo')
        
        empname = self.txt_emp_name.text()
        empPos = self.txt_position.text()
        empSara = self.txt_salary.text()
         
        add_emp = "insert into employee ('emp_name','positon','salary')valuse ('',empname,empPos,empSara)"
        cursor=conn.cursor()
        cursor.execute(add_emp)
        conn.commit()
        conn.close()
         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    toyo = QtWidgets.QMainWindow()
    ui = Ui_toyo()
    ui.setupUi(toyo)
    toyo.show()
    sys.exit(app.exec())
