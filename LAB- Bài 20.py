# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:41:17 2024

@author: DELL
"""
# Nhập vào 3 số a, b, c từ bàn phím. In ra màn hình số có giá trị lớn nhất không dùng hàm hỗ trợ)
a = int(input('Nhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
c = int(input('Nhập số nguyên c: '))
# so sánh a với b 
if a> b:
    max_value= a
else:
  max_value= b
# so sánh c với max
if c> max_value:
    max_value= c
    print('max_value:',max_value)
    
    



