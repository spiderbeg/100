# coding:utf8
import math
 
for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = math.sqrt(a * a + b * b)
        if c > 1000:
            break
        if c.is_integer():
            print(a, b, int(c))