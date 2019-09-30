#coding:utf-8
 
#筛法找素数: 
# 1. 建立一张表，用True，False标识一个数是否是素数。
# 2. 找到一个素数p，然后把p的倍数都标记成非素数。
# 3. 查表检测p + 1, 如果非素数检测下一个, 是素数执行1的操作
 
pt = [True] * 100
res = []
 
for p in range(2, 100):
    if not pt[p]: continue
    res.append(p)
    for i in range(p * p, 100, p):
        pt[i] = False
 
for i in range(1, len(res)):
    if res[i] - res[i-1] == 2:
        print (res[i-1], res[i])