# coding: utf8
def findArea(r):
    pi = 3.142
    return pi * (r*r)
r = int(input("请输入圆的半径"))
# 调用方法
print("圆的面积为 %.6f" % findArea(r)) 