# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:42:18 2024

@author: DELL
"""
# Viết chương trình cho phép nhập vào giờ, phút và giây theo định dạng hh:mm:ss. Hãy đổi ra giây và in kết quả ra màn hình
giờ = int(input( " Nhập số giờ: "))
phút = int(input(" Nhập số phút: "))
giây= int (input(" Nhập số giây: "))
if 0<=giờ<= 23 and phút<59 and giây <60:
    print(' Hiện tại là:',giờ,':',phút,':',giây)
    Tong_giay= giờ*3600+phút*60+giây
    print(" Tổng số giây là: ", Tong_giay)
else:
    print(" Nhập lại giờ, phút, giây")
    
