#coding:utf-8
 
# 1. 计算 n 的长度 l
# 2. 取n * n的后 l 位 t 
# 3. n == t ? 
 
for n in range(1, 10000):
    l = len(str(n))
    t = n * n % (10 ** l)
    if t == n:
        print(n)