# -*- coding: UTF-8 -*-
 
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
 
# 输出了第10个斐波那契数列
print('这是第10个月兔子总数 %d 只.'% (2*fib(10)))