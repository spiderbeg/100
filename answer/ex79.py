# coding:utf8
def sumOfFactors(k):
    p = 1
    q = k 
    s = 0
    while p < q:
        if k % p == 0:
            s += p + q 
        p += 1
        q = k / p 
 
    if k == p * q and p == q:
        s += p
 
    return s - k 
 
def fun(start, end):
    for x in range(start, end):
        y = sumOfFactors(x)
        if x < y and sumOfFactors(y) == x:
            print (x, y)
 
fun(2, 100000)