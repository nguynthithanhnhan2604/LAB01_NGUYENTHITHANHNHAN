# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:17:37 2024

@author: DELL
"""
# Viết chương trình đổi từ giờ/phút/giây thành giây.
giờ= int(input('Nhập giờ: '))
phút= int(input('Nhập phut: '))
giây= int(input('Nhập giây: '))
if 0<=giờ<=23 and 0<= phút<= 59 and 0<=giây<= 59:
    tong_giay= giờ* 60 + phút*60+ giây
    print('Tổng số giây là:',tong_giay)