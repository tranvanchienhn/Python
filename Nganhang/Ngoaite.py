from Buoi3.Nganhang.NganHang import *

class Giaodichngoaite(Giaodich):
    def __init__(self,_magiaodich,_ngaygiaodich,_dongia,_soluong,_tigia,_loaitiente):
        Giaodich.__init__(self, _magiaodich, _ngaygiaodich, _dongia, _soluong)
        self.tigia = _tigia
        self.loaitiente = _loaitiente
    def GetTiGia(self):
        return self.tigia
    def GetLoaitiente(self):
        return self.loaitiente

    def Thanhtien(self):
        if self.loaitiente == 'VND':
            return self.soluong * self.dongia
        else:
            return self.soluong * self.dongia * self.tigia
    def ToStringNgoaite(self):
        return str(self.GetMagiaodich()) +','+ str(self.GetNgaygiaodich()) +','+ str(self.GetDongia()) +','+ str(self.GetSoluong()) +','+ str(self.Thanhtien()) +'\n'
    def LuuGiaodichNgoaite(self):
        _file = open('Ngoaite.txt','a+')
        _file.write(self.ToStringNgoaite())
        _file.close()
    def DocfileNgoaite(self):
        _file = open('Ngoaite.txt','r+')
        _t = _file.read()
        _file.close()
        _list = []
        _list = _t.split(',')
        print(_list[1][1])