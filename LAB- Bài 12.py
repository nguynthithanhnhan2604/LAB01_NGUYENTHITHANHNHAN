# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:10:22 2024

@author: DELL
"""
import random 

#  Xuất ra một số (nguyên, thực) ngẫu nhiên theo yêu cầu
so = [random.choice([True, False]) for _ in range(4)]

# a) từ 0 đến 100
if so[0]: 
   a = round(random.uniform(0, 100),2)
else:
   a = random.randint(0,100)
print("Số ngẫu nhiên từ 0 đến 100 là:",a)
 # b) từ 50 đến 99 
if so[1]: 
   b = round(random.uniform(50, 99),2)
else:
   b = random.randint(50, 99)
print("Số ngẫu nhiên từ 50 đến 99 là:",b)


# c) từ -39 đến 79 
if so[2]: 
   c = round(random.uniform(-39, 79),2)
else:
   c = random.randint(-39, 79)

print("Số ngẫu nhiên từ -39 đến 79 là:",c)

# d)từ -79 đến -39
if so[3]: 
   d = round(random.uniform(-79, -39),2)
else:
   d = random.randint(-79, -39)
print("Số ngẫu nhiên từ -79 đến -39 là:",d)

    


