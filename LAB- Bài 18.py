# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:15:13 2024

@author: DELL
"""
# Viết chương trình cho 2 giờ (giờ, phút, giây) và thực hiện cộng, trừ 2 giờ
# Giờ thứ nhất
h1= int(input('Nhập giờ thứ nhất: '))
m1= int(input('Nhập phút thứ nhất: '))
s1= int(input('Nhập giây thứ nhất: '))
# Giờ thứ hai
h2= int(input('Nhập giờ thứ hai: '))
m2= int(input('Nhập phút thứ hai: '))
s2= int(input(' Nhập giây thứ hai: '))
if 0<=h1<=23 and 0<=m1<=59 and 0<=s1<=59 and 0<=h2<=23 and 0<=m2<=59 and 0<=s2<=59: 
# Cộng hai giờ 
 print('Tổng hai giờ là: ',h1+h2,'giờ',m1+m2,'phút',s1+s2,'giây')
# trừ hai gio
 print(' Hiệu hai giờ là: ', abs(h1-h2),'giờ',abs(m1-m2),'phút',abs(s1-s2),'giây')
else:
   print(' Bạn nhập không hợp lệ, mời nhập lại!')
