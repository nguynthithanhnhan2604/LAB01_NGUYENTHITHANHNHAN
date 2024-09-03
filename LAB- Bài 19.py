# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:43:31 2024

@author: DELL
"""
# . Nhập vào 4 số nguyên a, b, c, d. In ra màn hình số có giá trị nhỏ nhất (không dùng hàm min).
a = int(input('Nhập số nguyên a: '))
b = int(input('Nhập số nguyên b: '))
c = int(input('Nhập số nguyên c: '))
d = int(input('Nhập số nguyên d: '))
min_value = a
# So sánh b với min_value
if b < min_value:
    min_value = b
# So sánh c với min_value
if c < min_value:
    min_value = c
# So sánh d với min_value
if d < min_value:
    min_value = d
print('Giá trị nhỏ nhất là:', min_value)

    