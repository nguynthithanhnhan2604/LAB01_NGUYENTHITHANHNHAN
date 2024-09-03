# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 00:38:30 2024

@author: DELL
"""
# Viết chương trình nhập vào 2 số nguyên a, b. Tính tổng, hiệu, tích, thương 
a= int(input("Nhập số nguyên a:"))
b= int(input(" Nhập số nguyên b:"))
Tong=a+b
print(" Tổng của a,b là:",Tong)
Hieu=a-b
print(" Hiệu của a,b là:",Hieu)
Tích=a*b
print(" Tích của a,b là:",Tích)
#làm tròn 2 chữ số 
Thuong_2_chu_so= round(a/b,2)
print(" Thương của a,b là:", Thuong_2_chu_so)
#làm tròn 3 chữ số
Thuong_3_chu_so= round(a/b,3)
print(" Thương của a,b là:", Thuong_3_chu_so)



