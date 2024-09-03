# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:26:54 2024

@author: DELL
"""
# Viết chương trình cho phép nhập vào số nguyên dương N có 2 chữ số. Xuất ra màn hình tổng các chữ số của N.
N= int(input(' Nhập số nguyên N gồm 2 chữ số: '))
hang_chuc= N//10
hang_don_vi=N%10
tongN=hang_chuc+hang_don_vi
print('Tổng các chữ số của N là:',tongN)
