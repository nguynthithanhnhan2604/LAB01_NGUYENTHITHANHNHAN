# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:36:29 2024

@author: DELL
"""
#(a) Cho ba số a, b, c được nhập vào từ bàn phím. Hãy in ra màn hình theo thứ tự tăng dần các số (Chỉ dùng 1 biến phụ).

a= float(input(' Nhập giá trị của a: '))
b= float(input(' Nhập giá trị của b: '))
c= float(input(' Nhập giá trị của c: '))
if a> b:
    bien= a
    a=b
    b= bien
if a> c:
    bien= a
    a=c
    c= bien
if b>c:
    bien=b
    b=c
    c= bien
    print(' Già trị tăng dần các số là: ',a,b,c)

# (b) Nhập vào 1 số nguyên N sau đó in ra số có các con số theo thứ tự tăng dần. Ví dụ: nhập số 6879 thì in ra số 6789    
N= input('Nhập giá trị của N:')
if N.isdigit():
    ds = list(N)
    ds.sort()
    xep = "".join(ds)
    print(xep)
else:
    print("Vui lòng nhập lại một số nguyên")
