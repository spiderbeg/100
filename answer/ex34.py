# -*- coding: UTF-8 -*-

# 方法一
# for i in range(1,85):
#     if 168 % i == 0:
#         j = 168 / i
#         if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)

# 方法二
from math import sqrt
# sprt() 求平方根，返回浮点数，is_integer() 判断浮点数是否为整数
for i in range(-100,10000):
    if sqrt(i+100).is_integer() and sqrt(i+100+168).is_integer(): 
        print(i)
    