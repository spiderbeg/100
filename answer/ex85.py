# coding:utf8
 
import random
def fun():
    numa = [i for i in range(1, 34)]
    a = []
    for i in range(6):
        a.append(random.choice(numa))
        numa.remove(a[-1])
    a.append(random.choice([i for i in range(1, 17)]))
    print(a)
 
fun()