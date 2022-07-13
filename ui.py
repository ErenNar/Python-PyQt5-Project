from PyQt5 import uic

with open("ürün_ekle_app.py","w", encoding="utf-8" ) as fout:
    uic.compileUi("ürün.ui",fout)
