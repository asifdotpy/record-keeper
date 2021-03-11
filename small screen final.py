# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'small screen final.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QListWidget, QTableWidgetItem
from database import Database
from tableView import Ui_Form

#----------------------------------------Mainwondow--------------------------------------------------#

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 619)
        MainWindow.setFixedWidth(622)
        MainWindow.setFixedHeight(619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 621, 91))
        self.frame.setStyleSheet("background:#0dadd1;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #------------------------------------------------setting another window ----------------------------#
        self.secondWindow = None
        #----------------------------------------------------------------------------------------------------#
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 541, 61))
        self.label.setStyleSheet("font-size:46px; ")
        self.label.setObjectName("label")
        self.picLabel = QtWidgets.QLabel(self.centralwidget)
        self.picLabel.setGeometry(QtCore.QRect(16, 180, 51, 20))
        self.picLabel.setObjectName("picLabel")
        self.cameraFrame = QtWidgets.QFrame(self.centralwidget)
        self.cameraFrame.setGeometry(QtCore.QRect(80, 100, 181, 181))
        self.cameraFrame.setStyleSheet("border: 0.5px solid green;")
        self.cameraFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cameraFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cameraFrame.setObjectName("cameraFrame")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(20, 310, 41, 21))
        self.nameLabel.setObjectName("nameLabel")
        self.titleBox = QtWidgets.QComboBox(self.centralwidget)
        self.titleBox.setGeometry(QtCore.QRect(80, 310, 69, 22))
        self.titleBox.setStyleSheet("font-size:13px;\n"
"font-weight:bold;\n"
"")
        self.titleBox.setObjectName("titleBox")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.titleBox.addItem("")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(150, 310, 231, 22))
        self.nameEdit.setStyleSheet("font-size:15px;\n"
"font-weight:bold;\n"
"text-transform: capitalize;")
        self.nameEdit.setObjectName("nameEdit")
        #-------------------------------only int----------------------------------------#
        self.onlyInt = QtGui.QIntValidator()
        #-------------------------------------------------------------------------------#
        self.mobileLabel = QtWidgets.QLabel(self.centralwidget)
        self.mobileLabel.setGeometry(QtCore.QRect(20, 350, 41, 21))
        self.mobileLabel.setObjectName("mobileLabel")
        self.mobileEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mobileEdit.setGeometry(QtCore.QRect(80, 350, 301, 22))
        self.mobileEdit.setStyleSheet("font-size:15px;\n"
"font-weight:bold;\n"
"text-transform: capitalize;")
        self.mobileEdit.setObjectName("mobileEdit")
        self.mobileEdit.setValidator(self.onlyInt)
        self.itemLabel = QtWidgets.QLabel(self.centralwidget)
        self.itemLabel.setGeometry(QtCore.QRect(20, 380, 41, 21))
        self.itemLabel.setObjectName("itemLabel")
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(20, 410, 41, 21))
        self.dateLabel.setObjectName("dateLabel")
        self.dayBox = QtWidgets.QComboBox(self.centralwidget)
        self.dayBox.setGeometry(QtCore.QRect(80, 410, 51, 22))
        self.dayBox.setStyleSheet("font-size:13px;\n"
"font-weight:bold;\n"
"")
        self.dayBox.setObjectName("titleBox_2")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.dayBox.addItem("")
        self.monthBox = QtWidgets.QComboBox(self.centralwidget)
        self.monthBox.setGeometry(QtCore.QRect(220, 410, 41, 22))
        self.monthBox.setStyleSheet("font-size:13px;\n"
"font-weight:bold;\n"
"")
        self.monthBox.setObjectName("titleBox_3")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.monthBox.addItem("")
        self.yearBox = QtWidgets.QComboBox(self.centralwidget)
        self.yearBox.setGeometry(QtCore.QRect(320, 410, 60, 22))
        self.yearBox.setStyleSheet("font-size:13px;\n"
"font-weight:bold;\n"
"")
        self.yearBox.setObjectName("titleBox_4")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearBox.addItem("")
        self.yearLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearLabel.setGeometry(QtCore.QRect(280, 410, 41, 21))
        self.yearLabel.setObjectName("yearLabel")
        self.monthLabel = QtWidgets.QLabel(self.centralwidget)
        self.monthLabel.setGeometry(QtCore.QRect(150, 410, 41, 21))
        self.monthLabel.setObjectName("monthLabel")
        self.itemBox = QtWidgets.QComboBox(self.centralwidget)
        self.itemBox.setGeometry(QtCore.QRect(80, 380, 118, 22))
        self.itemBox.setStyleSheet("font-size:11px;\n"
"font-weight:bold;\n"
"")
        self.itemBox.setObjectName("itemBox")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.itemBox.addItem("")
        self.picesLabel = QtWidgets.QLabel(self.centralwidget)
        self.picesLabel.setGeometry(QtCore.QRect(200, 380, 41, 21))
        self.picesLabel.setStyleSheet("font-size:12;\n"
"font-weight:bold;")
        self.picesLabel.setObjectName("quantityLabel")
        self.piecesEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.piecesEdit.setGeometry(QtCore.QRect(240, 380, 35, 22))
        self.piecesEdit.setStyleSheet("font-size:15px;\n"
"font-weight:bold;\n"
"text-transform: capitalize;")
        self.piecesEdit.setObjectName("mobileEdit_2")
        self.piecesEdit.setValidator(self.onlyInt)
        self.priceLabel = QtWidgets.QLabel(self.centralwidget)
        self.priceLabel.setGeometry(QtCore.QRect(280, 380, 33, 21))
        self.priceLabel.setObjectName("priceLabel")
        self.mobileEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.mobileEdit_3.setGeometry(QtCore.QRect(1220, -90, 31, 22))
        self.mobileEdit_3.setStyleSheet("font-size:15px;\n"
"font-weight:bold;\n"
"text-transform: capitalize;")
        self.mobileEdit_3.setObjectName("mobileEdit_3")
        self.priceEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.priceEdit.setGeometry(QtCore.QRect(320, 380, 61, 22))
        self.priceEdit.setStyleSheet("font-size:15px;\n"
"font-weight:bold;\n"
"text-transform: capitalize;")
        self.priceEdit.setObjectName("priceEdit")
        self.priceEdit.setValidator(self.onlyInt)
        self.addressLabel = QtWidgets.QLabel(self.centralwidget)
        self.addressLabel.setGeometry(QtCore.QRect(10, 440, 61, 21))
        self.addressLabel.setObjectName("addressLabel")
        self.addressEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addressEdit.setGeometry(QtCore.QRect(80, 440, 301, 22))
        self.addressEdit.setStyleSheet("font-size:15px;\n"
"font-weight:bold;\n"
"text-transform: capitalize;")
        self.addressEdit.setObjectName("addressEdit")
        self.salesmanLabel = QtWidgets.QLabel(self.centralwidget)
        self.salesmanLabel.setGeometry(QtCore.QRect(10, 470, 61, 21))
        self.salesmanLabel.setObjectName("salesmanLabel")
        self.salesmanBox = QtWidgets.QComboBox(self.centralwidget)
        self.salesmanBox.setGeometry(QtCore.QRect(80, 470, 301, 22))
        self.salesmanBox.setStyleSheet("font-size:13px;\n"
"font-weight:bold;\n"
"")
        self.salesmanBox.setObjectName("salesmanBox")
        self.salesmanBox.addItem("")
        self.salesmanBox.addItem("")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(140, 510, 111, 51))
        self.saveBtn.setStyleSheet("background:#0fa1db;\n"
"font-size:15px;\n"
"font-weight:bold;")
        self.saveBtn.setObjectName("saveBtn")
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(360, 510, 111, 51))
        self.cancelBtn.setStyleSheet("background:#db0f49;\n"
"font-size:15px;\n"
"font-weight:bold;")
        self.cancelBtn.setObjectName("cancelBtn")
        self.recordsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.recordsBtn.setGeometry(QtCore.QRect(450, 140, 111, 71))
        self.recordsBtn.setStyleSheet("background:#4ae815;\n"
"font-size:15px;\n"
"font-weight:bold;")
        self.recordsBtn.setObjectName("recordsBtn")
        self.takeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.takeBtn.setGeometry(QtCore.QRect(280, 120, 71, 51))
        self.takeBtn.setStyleSheet("background:#98a39d;\n"
"font-size:15px;\n"
"font-weight:bold;")
        self.takeBtn.setObjectName("takeBtn")
        self.retakeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.retakeBtn.setGeometry(QtCore.QRect(280, 200, 71, 51))
        self.retakeBtn.setStyleSheet("background:#c0c73a;\n"
"font-size:15px;\n"
"font-weight:bold;")
        self.retakeBtn.setObjectName("retakeBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Salesman = QtWidgets.QAction(MainWindow)
        self.actionAdd_Salesman.setObjectName("actionAdd_Salesman")
        self.actionRemove_Salesman = QtWidgets.QAction(MainWindow)
        self.actionRemove_Salesman.setObjectName("actionRemove_Salesman")
        self.menuFile.addAction(self.actionAdd_Salesman)
        self.menuFile.addAction(self.actionRemove_Salesman)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #------------------------------------plus button added--------------------------------#
        self.plusBtn = QtWidgets.QPushButton(self.centralwidget)
        self.plusBtn.setGeometry(QtCore.QRect(383,377,31,31))
        self.plusBtn.setStyleSheet("border:0px;")
        self.plusBtn.setObjectName("plusBtn")
        self.plusBtn.setIcon(QtGui.QIcon("./images/plus-icon.png"))
        self.plusBtn.setIconSize(QtCore.QSize(25,25))
        self.plusBtn.clicked.connect(self.plusBtnfunc)
        self.index = 1
        #-------------------------------------------------------------------------------------#
        #----------------------------------Display console------------------------------------#
        self.displayList = QListWidget(self.centralwidget)
        self.displayList.setGeometry(QtCore.QRect(416, 260, 201, 218))
        self.displayList.setObjectName("displayList")

        #-------------------------------------------------------------------------------------#

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Noyon Kuthir Punjabi Ghar"))
        self.picLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Picture</span></p></body></html>"))
        self.nameLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Name</span></p></body></html>"))
        self.titleBox.setItemText(0, _translate("MainWindow", "Mr."))
        self.titleBox.setItemText(1, _translate("MainWindow", "Ms."))
        self.titleBox.setItemText(2, _translate("MainWindow", "Mrs."))
        self.mobileLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Mobile</span></p></body></html>"))
        self.itemLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Items</span></p></body></html>"))
        self.dateLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Date</span></p></body></html>"))
        self.dayBox.setItemText(0, _translate("MainWindow", "1"))
        self.dayBox.setItemText(1, _translate("MainWindow", "2"))
        self.dayBox.setItemText(2, _translate("MainWindow", "3"))
        self.dayBox.setItemText(3, _translate("MainWindow", "4"))
        self.dayBox.setItemText(4, _translate("MainWindow", "5"))
        self.dayBox.setItemText(5, _translate("MainWindow", "6"))
        self.dayBox.setItemText(6, _translate("MainWindow", "7"))
        self.dayBox.setItemText(7, _translate("MainWindow", "8"))
        self.dayBox.setItemText(8, _translate("MainWindow", "9"))
        self.dayBox.setItemText(9, _translate("MainWindow", "10"))
        self.dayBox.setItemText(10, _translate("MainWindow", "11"))
        self.dayBox.setItemText(11, _translate("MainWindow", "12"))
        self.dayBox.setItemText(12, _translate("MainWindow", "13"))
        self.dayBox.setItemText(13, _translate("MainWindow", "14"))
        self.dayBox.setItemText(14, _translate("MainWindow", "15"))
        self.dayBox.setItemText(15, _translate("MainWindow", "16"))
        self.dayBox.setItemText(16, _translate("MainWindow", "17"))
        self.dayBox.setItemText(17, _translate("MainWindow", "18"))
        self.dayBox.setItemText(18, _translate("MainWindow", "19"))
        self.dayBox.setItemText(19, _translate("MainWindow", "20"))
        self.dayBox.setItemText(20, _translate("MainWindow", "21"))
        self.dayBox.setItemText(21, _translate("MainWindow", "22"))
        self.dayBox.setItemText(22, _translate("MainWindow", "23"))
        self.dayBox.setItemText(23, _translate("MainWindow", "24"))
        self.dayBox.setItemText(24, _translate("MainWindow", "25"))
        self.dayBox.setItemText(25, _translate("MainWindow", "26"))
        self.dayBox.setItemText(26, _translate("MainWindow", "27"))
        self.dayBox.setItemText(27, _translate("MainWindow", "28"))
        self.dayBox.setItemText(28, _translate("MainWindow", "29"))
        self.dayBox.setItemText(29, _translate("MainWindow", "30"))
        self.dayBox.setItemText(30, _translate("MainWindow", "31"))
        self.monthBox.setItemText(0, _translate("MainWindow", "1"))
        self.monthBox.setItemText(1, _translate("MainWindow", "2"))
        self.monthBox.setItemText(2, _translate("MainWindow", "3"))
        self.monthBox.setItemText(3, _translate("MainWindow", "4"))
        self.monthBox.setItemText(4, _translate("MainWindow", "5"))
        self.monthBox.setItemText(5, _translate("MainWindow", "6"))
        self.monthBox.setItemText(6, _translate("MainWindow", "7"))
        self.monthBox.setItemText(7, _translate("MainWindow", "8"))
        self.monthBox.setItemText(8, _translate("MainWindow", "9"))
        self.monthBox.setItemText(9, _translate("MainWindow", "10"))
        self.monthBox.setItemText(10, _translate("MainWindow", "11"))
        self.monthBox.setItemText(11, _translate("MainWindow", "12"))
        self.yearBox.setItemText(0, _translate("MainWindow", "2021"))
        self.yearBox.setItemText(1, _translate("MainWindow", "2022"))
        self.yearBox.setItemText(2, _translate("MainWindow", "2023"))
        self.yearBox.setItemText(3, _translate("MainWindow", "2024"))
        self.yearBox.setItemText(4, _translate("MainWindow", "2025"))
        self.yearLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Year</span></p></body></html>"))
        self.monthLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Month</span></p></body></html>"))
        self.itemBox.setItemText(0, _translate("MainWindow", "Panjabi"))
        self.itemBox.setItemText(1, _translate("MainWindow", "Payjama"))
        self.itemBox.setItemText(2, _translate("MainWindow", "Serwani"))
        self.itemBox.setItemText(3, _translate("MainWindow", "Party Punjabi"))
        self.itemBox.setItemText(4, _translate("MainWindow", "Kids Punjabi"))
        self.itemBox.setItemText(5, _translate("MainWindow", "Gaye Holud Pun"))
        self.itemBox.setItemText(6, _translate("MainWindow", "Pagri"))
        self.itemBox.setItemText(7, _translate("MainWindow", "Nagra Juta"))
        self.itemBox.setItemText(8, _translate("MainWindow", "Rakhi"))
        self.itemBox.setItemText(9, _translate("MainWindow", "Goina Set"))
        self.itemBox.setItemText(10, _translate("MainWindow", "Rumal"))
        self.itemBox.setItemText(11, _translate("MainWindow", "Moja"))
        self.itemBox.setItemText(12, _translate("MainWindow", "Tupi"))
        self.itemBox.setItemText(13, _translate("MainWindow", "Stage,Car kpr"))
        self.itemBox.setItemText(14, _translate("MainWindow", "Gangy"))
        self.itemBox.setItemText(15, _translate("MainWindow", "Fotuwa"))
        self.itemBox.setItemText(16, _translate("MainWindow", "Party Spray"))
        self.itemBox.setItemText(17, _translate("MainWindow", "Baloon"))
        self.itemBox.setItemText(18, _translate("MainWindow", "Others"))
        self.picesLabel.setText(_translate("MainWindow", "<html><head/><body><p>Pieces</p></body></html>"))
        self.priceLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Price</span></p></body></html>"))
        self.addressLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Address</span></p></body></html>"))
        self.salesmanLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">SalesMan</span></p></body></html>"))
        self.salesmanBox.setItemText(0, _translate("MainWindow", "Sagir"))
        self.salesmanBox.setItemText(1, _translate("MainWindow", "Roton"))
        self.saveBtn.setText(_translate("MainWindow", "Save"))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.recordsBtn.setText(_translate("MainWindow", "All Records"))
        self.takeBtn.setText(_translate("MainWindow", "Take"))
        self.retakeBtn.setText(_translate("MainWindow", "Re-Take"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAdd_Salesman.setText(_translate("MainWindow", "Add Salesman"))
        self.actionRemove_Salesman.setText(_translate("MainWindow", "Remove Salesman"))

        #---------------------------cancel Button ---------------------------------#
        self.cancelBtn.clicked.connect(self.cancelBtnFunc)
        #-----------------------------save Button ---------------------------------#
        self.saveBtn.clicked.connect(self.saveBtnfunc)

        #-------------------------------records button--------------------------------------------------#
        self.recordsBtn.clicked.connect(self.show_new_window)

    def popUp(self, title, text):
        self.messageBox = QMessageBox()
        self.messageBox.setWindowTitle(title)
        self.messageBox.setText(text)
        self.messageBox.setStandardButtons(QMessageBox.Ok)
        self.messageBox.show()

    def cancelBtnFunc(self):
        self.nameEdit.clear()
        self.piecesEdit.clear()
        self.priceEdit.clear()
        self.mobileEdit.clear()
        self.displayList.clear()
        return self.addressEdit.clear()


    def saveBtnfunc(self):
        try:
            name = self.titleBox.currentText() + self.nameEdit.text()
            mobile = int(self.mobileEdit.text())
            products = self.itemBox.currentText()
            pieces = self.piecesEdit.text()
            price = self.priceEdit.text()
            day = self.dayBox.currentText()
            month = self.monthBox.currentText()
            year = self.yearBox.currentText()
            address = self.addressEdit.text()
            salesman = self.salesmanBox.currentText()
            db = Database(dbName="db.sqlite", tableName="data")
            db.add_data(name, mobile, products, pieces, price, day, month, year, address, salesman)
            self.popUp(title="Congratulations", text="Record added Successfully")
            self.index = 1
            self.displayList.clear()
            self.cancelBtnFunc()
        except:
            self.popUp(title="Warning", text="Please fill all the records")

    def show_new_window(self, checked):

        if self.secondWindow is None:
            self.Form = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.Form)
            self.Form.show()

        else:
            self.secondWindow.close()  # Close window.
            self.secondWindow = None  # Discard reference.

    def plusBtnfunc(self):
        self.displayList.addItem(str(self.index) + ". "+ self.itemBox.currentText() + " * " + self.piecesEdit.text() + " * " + self.priceEdit.text() + " = " + f"{int(self.piecesEdit.text()) * int(self.priceEdit.text())}")
        self.index += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
