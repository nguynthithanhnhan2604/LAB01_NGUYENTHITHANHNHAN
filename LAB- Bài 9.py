# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 00:56:21 2024

@author: DELL
"""

# In ra menu
print('==========MENU=========')
print('\t\t1. Hu tieu')
print('\t\t2. Chao long')
print('\t\t3. Bánh canh')
print('\t\t4. Bun rieu')
print('\t\t5. Pho bo')
print('=======================')
menu = ["1","2","3","4","5","hủ tiếu","cháo lòng","bánh canh", "bún riêu","phở bò"]
luachon= input('Mời nhập lựa chọn: ').lower()
if luachon in menu:
    print('=======================')
else:
    print('Mon khong co trong menu. Moi bạn nhap lai lua chon')