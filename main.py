
import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import *
from ürün_ekle_app import *
import sqlite3


        
app = QtWidgets.QApplication(sys.argv)
window= QtWidgets.QMainWindow()
ui = Ui_Form()   
ui.setupUi(window)
window.show()


ui.tableWidget.setHorizontalHeaderLabels(("ürün ad" , "ürün stok" , "ürün fiyat" , "ürün renk" ,"ürün tarih" ,"ürün marka" ,"ürün katagori"))

    
conn = sqlite3.connect("Product.db")
cursor = conn.cursor()
conn.commit()


createSQL ="create table if not exists  ProductTbl(p_name Text ,p_piece Int, p_price Int ,p_color Text , p_date Text , p_brand Text,p_catagory Text) "
cursor.execute(createSQL)
conn.commit()

def addProduct():
        
         p_name = ui.prdct_name.text()
         p_piece =int(ui.prdct_piece.text())
         p_price= int(ui.prdct_price.text())
         p_color = ui.prdct_color.text()
         p_date = ui.prdct_date.text()
         p_brand =ui.prdct_brand.currentText()
         p_catagory = ui.prdct_catagory.currentText()
         
         try:
             insertData = "insert into ProductTbl (p_name , p_piece , p_price,p_color,p_date,p_brand,p_catagory) values (?,?,?,?,?,?,?)"
             cursor.execute(insertData,(p_name,p_piece,p_price,p_color,p_date,p_brand,p_catagory))
            
             """  a = "select*from ProductTbl"
             b = cursor.execute(a)
             for i in b:
                 print(i)
             conn.commit()
            """
             allList()
             print(True)
         except Exception as err:
             print(False , err)
    

def allList():
    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(("ürün ad" , "ürün stok" , "ürün fiyat" , "ürün renk" ,"ürün tarih" ,"ürün marka" ,"ürün katagori"))
    listSql = "select*from ProductTbl"
    render=cursor.execute(listSql)
    
    for index1,item1  in enumerate(render):
        for inx2 , item2 in enumerate(item1):
            ui.tableWidget.setItem(index1,inx2,QTableWidgetItem(str(item2)))
    """""
    for index1, item1 in enumerate(cursor):
        for index2, item2 in enumerate(item1):
            ui.tableWidget.setItem(index1,index2,QTableWidgetItem(str(item2)))
    """
    conn.commit()


def filterList():
    ui.tableWidget.setHorizontalHeaderLabels(("ürün ad" , "ürün stok" , "ürün fiyat" , "ürün renk" ,"ürün tarih" ,"ürün marka" ,"ürün katagori"))
    tarih = ui.filterDate.currentIndex()
    marka = ui.filterBrand.currentText()
    fiyat = ui.filterPrice.currentText()
    if tarih==0:
        sql1="select * from ProductTbl order by p_date "
        a= cursor.execute(sql1)
        ui.tableWidget.setHorizontalHeaderLabels(("ürün ad" , "ürün stok" , "ürün fiyat" , "ürün renk" ,"ürün tarih" ,"ürün marka" ,"ürün katagori"))
        ui.tableWidget.clear()
        conn.commit()
        for index , item in enumerate(a):
            for index2 , item2 in enumerate(item):
                ui.tableWidget.setItem(index , index2, QTableWidgetItem(str(item2)))

    if tarih==1:
        sql2="select * from ProductTbl order by p_date desc "
        b= cursor.execute(sql2)
        ui.tableWidget.clear()
        ui.tableWidget.setHorizontalHeaderLabels(("ürün ad" , "ürün stok" , "ürün fiyat" , "ürün renk" ,"ürün tarih" ,"ürün marka" ,"ürün katagori"))
        conn.commit()
        for index , item in enumerate(b):
            for index2 , item2 in enumerate(item):
                ui.tableWidget.setItem(index , index2, QTableWidgetItem(str(item2)))


    if fiyat == 0:
        ui.tableWidget.setHorizontalHeaderLabels(("ürün ad" , "ürün stok" , "ürün fiyat" , "ürün renk" ,"ürün tarih" ,"ürün marka" ,"ürün katagori"))
        c= cursor.execute(sql3)
        ui.tableWidget.clear()
        sql3="select * from ProductTbl order by p_price desc  "
        conn.commit()
        for index , item in enumerate(c):
            for index2 , item2 in enumerate(item):
                ui.tableWidget.setItem(index , index2, QTableWidgetItem(str(item2)))
    if fiyat == 1 :
        ui.tableWidget.setHorizontalHeaderLabels(("ürün ad" , "ürün stok" , "ürün fiyat" , "ürün renk" ,"ürün tarih" ,"ürün marka" ,"ürün katagori"))
        d= cursor.execute(sql4 )
        ui.tableWidget.clear()
        sql4="select * from ProductTbl  order by p_price  "
        conn.commit()
        for index , item in enumerate(d):
            for index2 , item2 in enumerate(item):
                ui.tableWidget.setItem(index , index2, QTableWidgetItem(str(item2)))
   
    
    if marka:
        sql8="select * from ProductTbl where p_brand = ? "
        h= cursor.execute(sql8 , (marka ,))
        ui.tableWidget.clear()
        ui.tableWidget.setHorizontalHeaderLabels(("ürün ad" , "ürün stok" , "ürün fiyat" , "ürün renk" ,"ürün tarih" ,"ürün marka" ,"ürün katagori"))
        conn.commit()
        for index , item in enumerate(h):
            for index2 , item2 in enumerate(item):
                ui.tableWidget.setItem(index , index2, QTableWidgetItem(str(item2)))   

def removeProduct():
    sil_msg = QMessageBox.question(window,"silme işlemi","silmek istediğinizden emin misin" , QMessageBox.Yes | QMessageBox.No)
    
    if sil_msg ==QMessageBox.Yes:
        selected_item = ui.tableWidget.selectedItems()
        remove_item = selected_item[0].text()
        sql = "delete from ProductTbl p_name = ?"
        cursor.execute(sql,(remove_item ,))
        ui.tableWidget.clear()
        conn.commit()
    else:
        print("iptal edilfi")
def updateProduct():
          updt_message = QMessageBox.question(window,"güncelleme işlemi","güncellemek istediğinizden emin misin" , QMessageBox.Yes | QMessageBox.No)
          if updt_message == QMessageBox.Yes:
              try:
                p_name = ui.prdct_name.text()
                p_piece =int(ui.prdct_piece.text())
                p_price= int(ui.prdct_price.text())
                p_color = ui.prdct_color.text()
                p_date = ui.prdct_date.text()
                p_brand =ui.prdct_brand.currentText()
                p_catagory = ui.prdct_catagory.currentText()
                sql = "update ProductTbl set  p_piece=? , p_price=? , p_color=? , p_date=? , p_brand=? ,p_catagory=? where  p_name = ?"
                cursor.execute(sql, (p_piece,p_price,p_color,p_date,p_brand,p_catagory ,p_name))
                ui.tableWidget.clear()
                allList()
                conn.commit()
              except Exception as err:
                    print(err)
         

ui.deleteBtn.clicked.connect(removeProduct)
ui.updateBtn.clicked.connect(updateProduct)
ui.addBtn.clicked.connect(addProduct)
ui.allListBtn.clicked.connect(allList)
ui.filterBtn.clicked.connect(filterList)

sys.exit(app.exec_())
### yazılan ana kodlar 



