# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:02:40 2024

@author: DELL
"""
số_xe= int(input('Nhập số xe gồm 4 số: '))
số_dau= số_xe//1000
số_thứ_hai= số_xe//100- số_dau*10
số_thứ_ba= số_xe//10-(số_thứ_hai*10)-(số_dau*100)
số_thứ_tư= số_xe%10
if 999<số_xe<9999:
 Tổng_số_nút= số_dau+số_thứ_hai+số_thứ_ba+số_thứ_tư
 print('Tổng số nút của số xe gồm 4 chữ số là:',Tổng_số_nút)
else:
    print('Bạn đã nhập sai, mời nhập lại:')
    