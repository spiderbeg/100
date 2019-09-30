# -*- coding: UTF-8 -*-

l = []
while True:
    a = input('请输入数字')
    if a.isdigit() and int(a) % 2 ==0:
        l.append(int(a))
        if len(l) >= 3:
            new_l = sorted(l)
            print(new_l)
            break 