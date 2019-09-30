# coding:utf8
from functools import reduce

def fun(n):
    a = [int(c) for c in str(n)]
    a.sort()
 
    s1 = reduce(lambda x, y: 10 * x + y, a[::-1])
    s2 = reduce(lambda x, y: 10 * x + y, a)
 
    return n if s1 - s2 == n else fun(s1 - s2)
 
res = fun(6294)
print('res : ', res)