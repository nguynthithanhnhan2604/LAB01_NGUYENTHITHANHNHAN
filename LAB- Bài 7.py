# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:36:45 2024

@author: DELL
"""
# Nhập vào bán kính của hình tròn, tính và in ra chu vi, diện tích của hình tròn đó.
import math
bán_kính= float(input('Nhập bán kính hình tròn:'))
#Chu vi hình tron
chu_vi= round(bán_kính*math.pi,1)
print('Chu vi hình tròn là:', chu_vi)
#Diện tích hình tròn
dien_tich= round(bán_kính**2*math.pi,1)
print('Diện tích hình tròn là: ',dien_tich)

