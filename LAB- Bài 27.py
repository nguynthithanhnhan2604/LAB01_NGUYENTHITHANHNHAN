# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:54:44 2024

@author: DELL
"""
# Viết chương trình tính diện tích và chu vi các hình: hình vuông (v), hình chữ nhật (n) và hình tròn (t) với những thông tin được nhập từ bàn phím.
import math

hinh = input('Nhập hình (v là hình vuông, cn là hình chữ nhật, t là hình tròn): ')

# Chu vi, diện tích hình vuông
if hinh == "v":
    canh = float(input('Nhập độ dài cạnh: '))
    s_hinh_vuong = canh ** 2
    p_hinh_vuong = canh * 4
    print('Chu vi, diện tích hình vuông là:', p_hinh_vuong, s_hinh_vuong)

# Chu vi, diện tích hình chữ nhật
elif hinh == "cn":
    dai = float(input('Nhập chiều dài: '))
    rong = float(input('Nhập chiều rộng: '))
    s_hinh_cn = dai * rong
    p_hinh_cn = 2 * (dai + rong)
    print('Chu vi, diện tích hình chữ nhật là:', p_hinh_cn, s_hinh_cn)

# Chu vi, diện tích hình tròn
elif hinh == "t":
    ban_kinh = float(input('Nhập bán kính: '))
    s_hinh_tron = math.pi * ban_kinh ** 2
    p_hinh_tron = 2 * math.pi * ban_kinh
    print('Chu vi, diện tích hình tròn là:', p_hinh_tron, s_hinh_tron)

else:
    print('Bạn nhập không hợp lệ, mời nhập lại!')
