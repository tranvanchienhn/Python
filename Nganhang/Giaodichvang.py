from Buoi3.Nganhang.NganHang import *

class Giaodichvang(Giaodich):
    def __init__(self,_magiaodich,_ngaygiaodich,_dongia,_soluong,_loaivang):
        Giaodich.__init__(self,_magiaodich,_ngaygiaodich,_dongia,_soluong)
        self.loaivang = _loaivang
    def GetLoaivang(self):
        return self.loaivang

    def Thanhtien(self):
        return self.soluong * self.dongia

    def ToString(self):
        return str(self.GetMagiaodich()) +','+ str(self.GetNgaygiaodich()) +','+ str(self.GetDongia()) +','+ str(self.GetSoluong()) +','+ str(self.Thanhtien()) + '\n'
    def LuugiaodichVang(self):
        _file = open('Giaodichvang.txt','a+')
        _file.write(self.ToString())
        _file.close()
    def Docfile(self):
        _file = open('Giaodichvang.txt','r+')
        _t = _file.readlines()
        print(len(_t))
        _file.close()