# -*- coding: UTF-8 -*-

def SQ(x):
    return x * x
print('如果输入的数字平方小于 50，程序将停止运行。')
again = True
while again:
    num = int(input('请输入一个数字：'))
    print('运算结果为: %d' % (SQ(num))) 
    if SQ(num) <= 50:
        again = False
else:
    print('再见')