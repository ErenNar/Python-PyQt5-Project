# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ürün.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1205, 886)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setToolTipDuration(7)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("  font-family:\'Times New Roman\', Times, serif;\n"
"  background-color:rgb(17, 30, 58);\n"
"")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(70, 400, 317, 134))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.filterDate = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.filterDate.setStyleSheet("QComboBox{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:rgb(63, 101, 184);\n"
"    border: 1px solid white;\n"
"color:white;\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"}\n"
"QComboBox:focus{\n"
" background-color:rgb(63, 101, 184);\n"
"border:1px solid #002db3;\n"
"color:white;\n"
"}")
        self.filterDate.setObjectName("filterDate")
        self.filterDate.addItem("")
        self.filterDate.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.filterDate)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setStyleSheet("font-size:16px;\n"
"text-transform: uppercase;\n"
"font-weight:300;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.filterBrand = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.filterBrand.setStyleSheet("QComboBox{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:rgb(63, 101, 184);\n"
"    border: 1px solid white;\n"
"color:white;\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"}\n"
"QComboBox:focus{\n"
" background-color:rgb(63, 101, 184);\n"
"border:1px solid #002db3;\n"
"color:white;\n"
"}")
        self.filterBrand.setObjectName("filterBrand")
        self.filterBrand.addItem("")
        self.filterBrand.addItem("")
        self.filterBrand.addItem("")
        self.filterBrand.addItem("")
        self.filterBrand.addItem("")
        self.filterBrand.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.filterBrand)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setStyleSheet("font-size:16px;\n"
"text-transform: uppercase;\n"
"font-weight:300;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.filterPrice = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.filterPrice.setStyleSheet("QComboBox{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:rgb(63, 101, 184);\n"
"    border: 1px solid white;\n"
"color:white;\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"}\n"
"QComboBox:focus{\n"
" background-color:rgb(63, 101, 184);\n"
"border:1px solid #002db3;\n"
"color:white;\n"
"}")
        self.filterPrice.setObjectName("filterPrice")
        self.filterPrice.addItem("")
        self.filterPrice.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.filterPrice)
        self.filterBtn = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.filterBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filterBtn.setStyleSheet("QPushButton{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:#000000;\n"
"    font-size:16px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"background-color: #595959;    \n"
"\n"
"}")
        self.filterBtn.setObjectName("filterBtn")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.filterBtn)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setStyleSheet("font-size:16px;\n"
"text-transform: uppercase;\n"
"font-weight:300;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 20, 1041, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("font-size:32px;\n"
"text-transform: uppercase;\n"
"font-weight:900;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(400, 390, 721, 431))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidget.setStyleSheet("  font-family:\'Times New Roman\', Times, serif;\n"
"  background-color:rgb(63, 101, 184);\n"
"font-size:15px;\n"
"")
        self.tableWidget.setRowCount(20000)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(79, 90, 195))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 0, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 130, 1041, 244))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.rNAdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rNAdLabel.setStyleSheet("font-size:16px;\n"
"text-transform: uppercase;\n"
"font-weight:300;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.rNAdLabel.setObjectName("rNAdLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rNAdLabel)
        self.prdct_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.prdct_name.setStyleSheet("QLineEdit{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:rgb(63, 101, 184);\n"
"    border: 1px solid white;\n"
"color:white;\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"}\n"
"QLineEdit:focus{\n"
" background-color:white;\n"
"border:1px solid #002db3;\n"
"color:#002db3;\n"
"}")
        self.prdct_name.setText("")
        self.prdct_name.setObjectName("prdct_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.prdct_name)
        self.rNAdetiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rNAdetiLabel.setStyleSheet("font-size:16px;\n"
"text-transform: uppercase;\n"
"font-weight:300;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.rNAdetiLabel.setObjectName("rNAdetiLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rNAdetiLabel)
        self.prdct_piece = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.prdct_piece.setStyleSheet("QLineEdit{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:rgb(63, 101, 184);\n"
"    border: 1px solid white;\n"
"color:white;\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"}\n"
"QLineEdit:focus{\n"
" background-color:white;\n"
"border:1px solid #002db3;\n"
"color:#002db3;\n"
"}")
        self.prdct_piece.setText("")
        self.prdct_piece.setObjectName("prdct_piece")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.prdct_piece)
        self.rNFiyatLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rNFiyatLabel.setStyleSheet("font-size:16px;\n"
"text-transform: uppercase;\n"
"font-weight:300;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.rNFiyatLabel.setObjectName("rNFiyatLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.rNFiyatLabel)
        self.prdct_price = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.prdct_price.setStyleSheet("QLineEdit{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:rgb(63, 101, 184);\n"
"    border: 1px solid white;\n"
"color:white;\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"}\n"
"QLineEdit:focus{\n"
" background-color:white;\n"
"border:1px solid #002db3;\n"
"color:#002db3;\n"
"}")
        self.prdct_price.setText("")
        self.prdct_price.setObjectName("prdct_price")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.prdct_price)
        self.rNRengiLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rNRengiLabel.setStyleSheet("font-size:16px;\n"
"text-transform: uppercase;\n"
"font-weight:300;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.rNRengiLabel.setObjectName("rNRengiLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.rNRengiLabel)
        self.prdct_color = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.prdct_color.setStyleSheet("QLineEdit{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:rgb(63, 101, 184);\n"
"    border: 1px solid white;\n"
"color:white;\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"}\n"
"QLineEdit:focus{\n"
" background-color:white;\n"
"border:1px solid #002db3;\n"
"color:#002db3;\n"
"}")
        self.prdct_color.setText("")
        self.prdct_color.setObjectName("prdct_color")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.prdct_color)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font-size:16px;\n"
"text-transform: uppercase;\n"
"font-weight:300;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.prdct_date = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.prdct_date.setToolTipDuration(0)
        self.prdct_date.setStyleSheet("QDateEdit{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:rgb(63, 101, 184);\n"
"    border: 1px solid white;\n"
"color:white;\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"}\n"
"QDateEdit:focus{\n"
" background-color:white;\n"
"border:1px solid #002db3;\n"
"color:#002db3;\n"
"}")
        self.prdct_date.setCurrentSectionIndex(0)
        self.prdct_date.setDate(QtCore.QDate(2022, 1, 1))
        self.prdct_date.setObjectName("prdct_date")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.prdct_date)
        self.prdct_brand = QtWidgets.QComboBox(self.formLayoutWidget)
        self.prdct_brand.setStyleSheet("QComboBox{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:rgb(63, 101, 184);\n"
"    border: 1px solid white;\n"
"color:white;\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"}\n"
"QComboBox:focus{\n"
" background-color:rgb(63, 101, 184);\n"
"border:1px solid #002db3;\n"
"color:white;\n"
"}")
        self.prdct_brand.setObjectName("prdct_brand")
        self.prdct_brand.addItem("")
        self.prdct_brand.addItem("")
        self.prdct_brand.addItem("")
        self.prdct_brand.addItem("")
        self.prdct_brand.addItem("")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.prdct_brand)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font-size:16px;\n"
"text-transform: uppercase;\n"
"font-weight:300;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setStyleSheet("font-size:16px;\n"
"text-transform: uppercase;\n"
"font-weight:300;\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"color:white")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.prdct_catagory = QtWidgets.QComboBox(self.formLayoutWidget)
        self.prdct_catagory.setStyleSheet("QComboBox{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:rgb(63, 101, 184);\n"
"    border: 1px solid white;\n"
"color:white;\n"
"font-size:16px;\n"
"border-radius:6px;\n"
"}\n"
"QComboBox:focus{\n"
" background-color:rgb(63, 101, 184);\n"
"border:1px solid #002db3;\n"
"color:white;\n"
"}")
        self.prdct_catagory.setObjectName("prdct_catagory")
        self.prdct_catagory.addItem("")
        self.prdct_catagory.addItem("")
        self.prdct_catagory.addItem("")
        self.prdct_catagory.addItem("")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.prdct_catagory)
        self.addBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addBtn.setStyleSheet("QPushButton{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:#000000;\n"
"    font-size:16px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"background-color: #595959;    \n"
"\n"
"}")
        self.addBtn.setObjectName("addBtn")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.addBtn)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(70, 590, 311, 151))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.allListBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.allListBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.allListBtn.setStyleSheet("QPushButton{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:#000000;\n"
"    font-size:16px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"background-color: #595959;    \n"
"cursor:pointer;\n"
"}")
        self.allListBtn.setObjectName("allListBtn")
        self.verticalLayout_3.addWidget(self.allListBtn)
        self.deleteBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.deleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteBtn.setStyleSheet("QPushButton{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:#000000;\n"
"    font-size:16px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"background-color: #595959;    \n"
"\n"
"}")
        self.deleteBtn.setObjectName("deleteBtn")
        self.verticalLayout_3.addWidget(self.deleteBtn)
        self.updateBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.updateBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.updateBtn.setStyleSheet("QPushButton{\n"
"font-family:\'Times New Roman\', Times, serif;\n"
"    background-color:#000000;\n"
"    font-size:16px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"background-color: #595959;    \n"
"\n"
"}")
        self.updateBtn.setObjectName("updateBtn")
        self.verticalLayout_3.addWidget(self.updateBtn)

        self.retranslateUi(Form)
        self.filterDate.setCurrentIndex(-1)
        self.filterBrand.setCurrentIndex(-1)
        self.filterPrice.setCurrentIndex(-1)
        self.prdct_brand.setCurrentIndex(-1)
        self.prdct_catagory.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.filterDate.setItemText(0, _translate("Form", "Eskiden Yeniye"))
        self.filterDate.setItemText(1, _translate("Form", "Yeniden Eskiye"))
        self.label_7.setText(_translate("Form", "marakya göre listele"))
        self.filterBrand.setItemText(0, _translate("Form", "Arçelik"))
        self.filterBrand.setItemText(1, _translate("Form", "Hp"))
        self.filterBrand.setItemText(2, _translate("Form", "Vestel"))
        self.filterBrand.setItemText(3, _translate("Form", "Beko"))
        self.filterBrand.setItemText(4, _translate("Form", "Samsung"))
        self.filterBrand.setItemText(5, _translate("Form", "Arçelik"))
        self.label_8.setText(_translate("Form", "fiyata göre listele"))
        self.filterPrice.setItemText(0, _translate("Form", "Artan Fiyat"))
        self.filterPrice.setItemText(1, _translate("Form", "Azalan Fiyat"))
        self.filterBtn.setText(_translate("Form", "SIRALA"))
        self.label_6.setText(_translate("Form", "tarihe göre listele"))
        self.label.setText(_translate("Form", "ürün uygulaması"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.rNAdLabel.setText(_translate("Form", "ürün adı"))
        self.rNAdetiLabel.setText(_translate("Form", "ürün adeti"))
        self.rNFiyatLabel.setText(_translate("Form", "ürün fiyatı"))
        self.rNRengiLabel.setText(_translate("Form", "ürün rengi"))
        self.label_2.setText(_translate("Form", "ürün tarihi"))
        self.prdct_brand.setItemText(0, _translate("Form", "Arçelik"))
        self.prdct_brand.setItemText(1, _translate("Form", "Beko"))
        self.prdct_brand.setItemText(2, _translate("Form", "Samsung"))
        self.prdct_brand.setItemText(3, _translate("Form", "Hp"))
        self.prdct_brand.setItemText(4, _translate("Form", "Vestel"))
        self.label_3.setText(_translate("Form", "ürün markası"))
        self.label_4.setText(_translate("Form", "ürün kategorisi"))
        self.prdct_catagory.setItemText(0, _translate("Form", "Telefon"))
        self.prdct_catagory.setItemText(1, _translate("Form", "Televizyon"))
        self.prdct_catagory.setItemText(2, _translate("Form", "Buzdolabı"))
        self.prdct_catagory.setItemText(3, _translate("Form", "Çamaşır Makinesi"))
        self.addBtn.setText(_translate("Form", "ÜRÜN EKLE"))
        self.allListBtn.setText(_translate("Form", "TÜMÜNÜ LİSTLELE"))
        self.deleteBtn.setText(_translate("Form", "ÜRÜN SİL"))
        self.updateBtn.setText(_translate("Form", "ÜRÜN GÜNCELLE"))

