# coding:utf8
import math
def FindHim():
    for x in range(10):
        for y in range(10):
            if x != y:
                result = x * 1100 + y * 11
                test = math.sqrt(result) 
                if test.is_integer():
                    return result
 
print (FindHim())