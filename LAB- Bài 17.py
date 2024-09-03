# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:06:49 2024

@author: DELL
"""
# Cho 3 số nguyên. Cho biết số lớn nhất và nhỏ nhất?
so_thu_nhat= int(input(' Nhập số nguyên thứ nhất: '))
so_thu_hai= int(input(' Nhập số nguyên thứ hai: '))
so_thu_ba= int(input(' Nhập số nguyên thứ ba: '))
# Số lớn nhất
so_lon_nhat= max(so_thu_nhat,so_thu_hai,so_thu_ba)
print(' Số lớn nhất trong 3 số là:', so_lon_nhat)
# Số nhỏ nhất
so_nho_nhat= min(so_thu_nhat,so_thu_hai,so_thu_ba)
print(' Số nhỏ nhất trong 3 số là:', so_nho_nhat)
