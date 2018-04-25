import math
import list
import copy
_t = int(input('Nhập bài tập cần tính:'))
if _t == 1:
    _n = int(input('Nhập vào số N: '))
    if _n < 50:
        print('Số vừa nhập vào nhỏ hơn 50')
    else:
        print('Số vừa nhập vào lớn hơn 50')
elif _t == 2:
    _d1 = float(input('Nhập vào điểm môn toán: '))
    _d2 = float(input('Nhập vào điểm môn lý: '))
    _d3 = float(input('Nhập vào điểm môn Hoá: '))
    if _d1 + _d2 + _d3 >=15 and _d1 >4 and _d2 >4 and _d3 > 4:
        print('Đậu')
    else:
        print('Trượt')
elif _t == 3:
    _n = int(input('Nhập N: '))
    _sum = 0
    for _i in range(1,_n+1):
        _sum = _sum + math.pow(_i,2)
    print('Tổng là:',_sum)
elif _t == 4:
    _n = int(input('Nhập N: '))
    _list = []
    if _n > 100:
        print('Số bạn nhập không hợp lệ')
    else:
        for _i in range(1,_n+1):
            if _i%2 == 0:
                _list.append(_i)
        print(_list)
elif _t == 5:
    _a = int(input('Nhập vào cạnh A: '))
    _b = int(input('Nhập vào cạnh B: '))
    _c = int(input('Nhập vào cạnh C: '))
    if _a + _b > _c and _a + _c > _b and _c + _b > _a and _a > 0 and _b > 0 and _c > 0:
        print('Đây là độ dài 3 cạnh của tam giác')
        if _a == _b or _b == _c or _a == _c:
            print('Đây là tam giác cân')
        elif _a == _b == _c:
            print('Đây là tam giác đều')
        elif _a*_a + _b*_b == _c*_c or _a*_a + _c*_c == _b*_b or _b*_b + _c*_c == _a*_a:
            print('Đây là tam giác vuông')
    else:
        print('Đây không phải là 3 cạnh của tam giác')
elif _t == 6:
    _a = int(input('Nhập vào số thứ nhất: '))
    _b = int(input('Nhập vào số thứ hai: '))
    _c = int(input('Nhập vào số thứ ba: '))
    _list = [_a,_b,_c]
    print('Số lớn nhất là:',max(_list))
    print('Số nhỏ nhất là:',min(_list))
elif _t == 7:
    for _i in range(0,7):
        if _i == 3:
             continue
        if _i == 6:
            continue
        print(_i)
elif _t == 8:
    _str = input('Nhập vào một chuỗi: ')
    print('Chuỗi đảo ngược là:',_str[::-1])
elif _t == 9:
    _n = float(input('Nhập vào điểm trung bình của học sinh: '))
    if _n < 0 or _n > 10:
        print('Điểm bạn nhập vào không chính xác')
    else:
        if _n >= 9:
            print('Xếp hạng A')
        elif 7 <= _n < 9:
            print('Xếp hạng B')
        elif 5 <= _n < 7:
            print('Xếp hạng C')
        else:
            print('Xếp hạng F')
elif _t == 10:
    _list = ['abc','xyz','abc',12,'ii',12,'5a']
    _listmoi = []
    for _i in _list:
        if _list.count(_i) == 1:
            _listmoi.append(_i)
    print(_listmoi)
elif _t == 11 or _t == 12:
    _list = [11,2,31,213,12,41,513,121,1]
    print('Số lớn nhất là:',max(_list))
    print('Số nhỏ nhất là:',min(_list))
elif _t == 13:
    _list = [11, 2, 31, 213, 12, 41, 513, 121, 1]
    _listmoi = _list[:]
    print(_listmoi)
elif _t == 14:
    _list = ['1131','qwerad','12','242e23','daeedadda','1','aa','44']
    _n = int(input('Nhập vào N: '))
    for _i in _list:
        if _n < len(_i):
            print(_i)