# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 02:07:43 2024

@author: DELL
"""
import math
# Giải và biện luận phương trình bậc hai: ax2 + bx + c = 0
a= float(input('Nhập giá trị của a: '))
b= float(input('Nhập giá trị cho b: '))
c= float(input('Nhập giá trị cho c: '))
delta = (b**2) - (4*a*c)
if a>0 :
    print(' Phương trình có 2 nghiệm:', (-b+ math.sqrt(delta)/2*a),'và',(-b - math.sqrt(delta)/2*a))
elif a==0:
    print('Phươgn trình có nghiệm kép: ',-b/ 2*a)
else:
    print('Phươbg trình vô nghiệm')
    