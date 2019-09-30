# coding:utf8

def isPrimeNumber(n, s):
    for k in s: 
        if k ** 2 > n: break
        if n % k == 0: return False
    return True
 
def fun():
    s = [3]
    for n in range(6, 100000, 2):
        f = False
        for k in s:  
            t = n - k
            if t < k:
                break
            if isPrimeNumber(t, s):
                #print '%s = %s + %s' % (n, k, t)
                if t > s[-1]: s.append(t)
                f = True
                break
        if not f: 
            raise Exception