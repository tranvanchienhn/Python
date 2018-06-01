from Buoi3.Nganhang import NganHang,Ngoaite,Giaodichvang

_k = int(input('Nhập loại giao dịch, ấn 1 nhập giao dịch vàng - ấn 2 nhập giao dịch ngoại tệ: '))
if _k == 1:
    _n = int(input('Nhập số lượng giao dịch: '))
    for _i in range(_n):
        print('Nhập giao dịch thứ ',_i + 1,':')
        _magiaodich = input('Nhập mã giao dịch: ')
        _ngaygiaodich = input('Nhập ngày giao dịch: ')
        _dongia = int(input('Nhập đơn giá: '))
        _soluong = int(input('Nhập số lượng: '))
        _loaivang = input('Nhập loại vàng: ')
        _vang = Giaodichvang.Giaodichvang(_magiaodich,_ngaygiaodich,_dongia,_soluong,_loaivang)
        _vang.LuugiaodichVang()
    _vang.Docfile()
elif _k == 2:
    _n = int(input('Nhập số lượng giao dịch: '))
    for _i in range(_n):
        print('Nhập giao dịch thứ ', _i + 1, ':')
        _magiaodich = input('Nhập mã giao dịch: ')
        _ngaygiaodich = input('Nhập ngày giao dịch: ')
        _dongia = int(input('Nhập đơn giá: '))
        _soluong = int(input('Nhập số lượng: '))
        _tygia = input('Nhập tỷ giá: ')
        _loaitiente = input('Nhập loại tiền tệ: ')
        _ngoaite = Ngoaite.Giaodichngoaite(_magiaodich,_ngaygiaodich,_dongia,_soluong,_tygia,_loaitiente)
        _ngoaite.LuuGiaodichNgoaite()
    _ngoaite.DocfileNgoaite()