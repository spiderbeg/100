# -*- coding: UTF-8 -*-

a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
d = [a,b,c]
d.sort()
if d[0] + d[1] > d[-1]:
    # 计算半周长
    s = (a + b + c) / 2
    # 计算面积
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print('三角形面积为 %0.2f' %area)
else:
    print('请注意三角形两边之和大于第三边')