# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:14:22 2024

@author: DELL
"""
# Nhập 1 số bất kỳ. Hãy in giá trị (chuỗi) của số nguyên đó nếu nó có giá trịtừ 0 đến 9, ngược lại thông báo không đọc được.
số= int(input('Nhập một số bất kì từ 0 tới 9: '))
chuỗi= ['Không','Một','Hai','Ba','Bốn','Năm','Sáu','Bảy','Tám','Chín']
if 0<= số <= 9:
    print( 'Số nguyên bạn nhập là:',chuỗi[số])
else:
    print('Không đọc được, mời bnaj nhập lại:')