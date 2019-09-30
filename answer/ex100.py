#coding:utf-8
def fun():
    for i in range(0, 100, 3):
        for j in range(100):
            if 100 - i - j >= 0 and 5*(100 - i - j) + i/3 + j == 100 and (i/3 + j)%5 == 0:
                print ('小鸡%d只，母鸡%d只，公鸡%d只'%(i, j, 100 - i - j))

fun()