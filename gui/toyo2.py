# Form implementation generated from reading ui file 'toyo2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as cn

class Ui_toyo(object):
    def setupUi(self, toyo):
        toyo.setObjectName("toyo")
        toyo.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(26)
        toyo.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=toyo)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_emp_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_emp_name.setGeometry(QtCore.QRect(10, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(36)
        self.lbl_emp_name.setFont(font)
        self.lbl_emp_name.setObjectName("lbl_emp_name")
        self.lbl_position = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_position.setGeometry(QtCore.QRect(10, 90, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(36)
        self.lbl_position.setFont(font)
        self.lbl_position.setObjectName("lbl_position")
        self.lbl_salary = QtWidgets.QLabel(parent=self.centralwidget)
        self.lbl_salary.setGeometry(QtCore.QRect(20, 160, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(36)
        self.lbl_salary.setFont(font)
        self.lbl_salary.setObjectName("lbl_salary")
        self.btnAdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(230, 240, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(26)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(self.add_emp) 
        self.btnClear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(400, 240, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(26)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 310, 611, 192))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(20)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.txt_emp_name = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_emp_name.setGeometry(QtCore.QRect(190, 10, 351, 61))
        self.txt_emp_name.setObjectName("txt_emp_name")
        self.txt_position = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_position.setGeometry(QtCore.QRect(190, 80, 351, 61))
        self.txt_position.setObjectName("txt_position")
        self.txt_salary = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_salary.setGeometry(QtCore.QRect(190, 160, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Angsana New")
        font.setPointSize(26)
        self.txt_salary.setFont(font)
        self.txt_salary.setObjectName("txt_salary")
        toyo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=toyo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 42))
        self.menubar.setObjectName("menubar")
        toyo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=toyo)
        self.statusbar.setObjectName("statusbar")
        toyo.setStatusBar(self.statusbar)

        self.retranslateUi(toyo)
        self.btnClear.clicked.connect(self.txt_salary.clear) # type: ignore
        self.btnClear.clicked.connect(self.txt_position.clear) # type: ignore
        self.btnClear.clicked.connect(self.txt_emp_name.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(toyo)

    def retranslateUi(self, toyo):
        _translate = QtCore.QCoreApplication.translate
        toyo.setWindowTitle(_translate("toyo", "โปรแกรมเพิ่มข้อมูลพนังงาน"))
        self.lbl_emp_name.setText(_translate("toyo", "ชื่อพนักงาน"))
        self.lbl_position.setText(_translate("toyo", "ตำแหน่ง"))
        self.lbl_salary.setText(_translate("toyo", "เงินเดือน"))
        self.btnAdd.setText(_translate("toyo", "เพิ่มข้อมูล"))
        self.btnClear.setText(_translate("toyo", "ยกเลิก"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("toyo", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("toyo", "Position"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("toyo", "EmpName"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("toyo", "Salary"))

    def add_emp(self):
        conn = cn.connect(user='root',
        password='',
        host='localhost',
        database='toyo')
        cursor=conn.cursor()
        empname=self.txt_emp_name.text()
        posit=self.txt_position.text()
        salary=self.txt_salary.text()
        insert="INSERT INTO employee(emp_name,position,salary) values(%s,%s,%s)"
        val = (empname,posit,salary)
        cursor.execute(insert,val)
        conn.commit
        conn.close
        self.txt_emp_name.clear()
        self.txt_position.clear()
        self.txt_salary.clear()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    toyo = QtWidgets.QMainWindow()
    ui = Ui_toyo()
    ui.setupUi(toyo)
    toyo.show()
    sys.exit(app.exec())
