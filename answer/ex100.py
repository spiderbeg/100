#公鸡 5 钱 , 母鸡 3 钱, 小鸡 1/3 钱。要求：100只鸡 100文钱
#coding:utf-8
def fun():
    for i in range(0, 100, 3): # i 母鸡总价
        for j in range(0,100,5): # j 公鸡总价
            s = 100 - i - j # s 小鸡总价
            if s >= 0 and s*3 + i//3 + j//5 == 100: # 判断鸡的数量等于100
                print ('小鸡%d只，母鸡%d只，公鸡%d只'%(s*3, i//3, j//5))

fun()