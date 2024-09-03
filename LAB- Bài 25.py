# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:18:42 2024

@author: DELL
"""
#Nhập 1 chữ cái, nếu là chữ thường thì đổi thành chữ hoa, ngược lại đổi thành chữ thường.

chu_cái= input(' Nhập một chữ cái: ')
if len(chu_cái)==1 and chu_cái.isalpha(): 
 if chu_cái.isupper() :
    print(' Chữ in thường tương ứng là:', chu_cái.lower())
 if chu_cái.islower():
    print(' Chữ in hoa tương ứng là: ', chu_cái.upper())
else:
    print('Bạn nhập không hợp lệ, mời nhập lại!')