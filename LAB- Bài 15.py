# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:44:25 2024

@author: DELL
"""
# Nhập hai số a, b. Sau đó, tính toán biểu thức s
import math
a= float(input('Nhập số a: '))
b= float(input('Nhập số b: '))
Bieu_thuc= ((a+b)/ (math.pow(a,1/3)+math.pow(b,1/3))-( math.pow(a*b,1/3))) / ((math.pow(a,1/3)-math.pow(b,1/3))**2)
ket_qua= round(Bieu_thuc,3)
print('Kết quả của biểu thức là:', ket_qua)
