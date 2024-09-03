# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 01:56:15 2024

@author: DELL
"""
# Nhập lần lượt ngày, tháng, năm sinh. Sau đó xuất ra theo định dạng
# Nhập ngày tháng năm
ngay = int(input('Nhập ngày sinh: '))
thang = int(input('Nhập tháng sinh: '))
nam = int(input('Nhập năm sinh: '))

# Kiểm tra năm nhuận
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    nam_nhuan = True
else:
    nam_nhuan = False

# Số ngày tối đa trong từng tháng
ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if nam_nhuan:
    ngay_trong_thang[1] = 29 

# Kiểm tra tính hợp lệ của ngày, tháng, năm
if 1 <= thang <= 12 and 1 <= ngay <= ngay_trong_thang[thang - 1] and nam > 0:
# a) Xuất định dạng dd/mm/yyyy
    print('a. dd/mm/yyyy')
    ngay_thang_nam_a = f"{ngay}/{thang}/{nam}"
    print('Ngày tháng năm sinh của bạn là:', ngay_thang_nam_a)

# Làm ngược lại
    ngay_a, thang_a, nam_a = map(int, ngay_thang_nam_a.split("/"))
    print(f"Ngày {ngay_a} \nTháng {thang_a} \nNăm {nam_a}")

# b) Xuất định dạng dd/mm/yy
    print('b. dd/mm/yy')
    nam_b = nam % 100
    ngay_thang_nam_b = f"{ngay}/{thang}/{nam_b:02}"
    print('Ngày tháng năm sinh của bạn là:', ngay_thang_nam_b)

# Làm ngược lại
    ngay_b, thang_b, nam_b = map(int, ngay_thang_nam_b.split("/"))
    if 0 <= nam_b <= 25:
        print(f"Ngày {ngay_b} \nTháng {thang_b} \nNăm", nam_b + 2000)
    else:
        print(f"Ngày {ngay_b} \nTháng {thang_b} \nNăm", nam_b + 1900)

# c) Xuất định dạng yyyy/mm/dd
    print('c. yyyy/mm/dd')
    ngay_thang_nam_c = f"{nam}/{thang}/{ngay}"
    print('Ngày tháng năm sinh của bạn là:', ngay_thang_nam_c)

# Làm ngược lại
    nam_c, thang_c, ngay_c = map(int, ngay_thang_nam_c.split("/"))
    print(f"Ngày {ngay_c} \nTháng {thang_c} \nNăm {nam_c}")
else:
    print("Ngày tháng năm không tồn tại. Vui lòng nhập lại ngày tháng năm hợp lệ.")

      