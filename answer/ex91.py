#coding:utf-8
 
# 解题步骤：
#    1. 用筛法找到900以内素数表
#    2. 迭代表内所有数，是素数的检测它的反序数是否是素数。
#    3. 2条件为真，打印这俩个素数。
 
def getPrimeTable(n):
    pt = [True] * n
 
    for p in range(2, n):
        if not pt[p]: continue
        for i in range(p * p, n, p):
            pt[i] = False
 
    return pt
 
pt = getPrimeTable(900)
print(len(pt))
for p in range(2, 900):
    if not pt[p]: continue
    q = int(str(p)[::-1])
    if q < 900 and pt[q]:
        pt[q] = False 
        print (p, q)