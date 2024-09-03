# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 02:33:55 2024

@author: DELL
"""
# Nhập vào giờ, phút, giây. Kiểm tra xem giờ, phút, giây đó có hợp lệ hay không?
giờ= int(input(' Nhập giờ: '))
phút= int(input('Nhập phút: '))
giây= int(input('Nhập giây: '))
if 0<= giờ<= 23 and 0<= phút<= 59 and 0<= giây <= 59:
    print(' Bây giờ là:', giờ,'giờ',phút,'phút',giây,'giây')
else:
    print(' Thời gian nhập không hợp lệ, mời bạn nhập lại:')
    