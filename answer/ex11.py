# encoding:utf8
#打印空心倒三角形
 
for i in range(1,6):
    for j in range(i+1,7):
        if j > 1+i and j <6 and i >1:
            print(" " ,end=" ")
        else:
            print("*",end=" ")
    print()