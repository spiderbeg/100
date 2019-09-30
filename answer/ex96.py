#coding:utf-8
 
# 解题步骤:
#    1. 筛法找到100所有素数
#    2. 对于素数list内素有俩两组合，构造等差数列a0, a1项
#    3. 计算出a2， 查表判断a2是否是素数，是素数则能构成素数等差序列， 计算a3...
 
def findAllPrime(n):
    pt = [True] * n
    prime = []
 
    for p in range(2, n):
        if not pt[p]: continue
        prime.append(p)
        for i in range(p * p, n, p):
            pt[i] = False
 
    return prime, pt
 
prime, pt = findAllPrime(100)
print (prime)
 
for i in range(len(prime)):
    for j in range(i + 1, len(prime)):
        a0, a1 = prime[i], prime[j]
        an = a1 + a1 - a0
        s = []
        while an < 100 and pt[an]:
            s.append(an)
            an += a1 - a0
        if s:
            print ([a0, a1] + s)