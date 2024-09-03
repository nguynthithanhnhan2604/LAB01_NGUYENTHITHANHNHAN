# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:36:48 2024

@author: DELL
"""

# Viết chương trình tính số đo kiểm tra sức khỏe BMI.
cân_nặng= float(input('Nhập cân nặng của bạn: '))
chiều_cao= float(input('Nhập chiều cao của bạn: '))
BMI= cân_nặng/chiều_cao**2
if chiều_cao>0 and cân_nặng>0:
    print('Chỉ số BMI của bạn là: ',BMI)
else:
    print('Nhập lại chiều cao, cân nặng của bạn')
    
    