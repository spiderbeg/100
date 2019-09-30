# -*- coding: UTF-8 -*-
 
a = int(input("请输入一个数字:\n"))
x = str(a)
flag = True
 
for i in range(len(x)//2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print("%d 是一个回文数!" % a)
else:
    print("%d 不是一个回文数!" % a)