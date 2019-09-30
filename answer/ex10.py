# encoding:utf8

#打印实心倒金字塔
for i in range(1,6):
    for k in range(i-1):
        print(end=" ")
    for j in range(6-i):
        print("*",end=" ")
    print()
