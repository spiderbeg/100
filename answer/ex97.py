# coding:utf
import random
 
score = [random.randint(1,100) for x in range(10)]
 
print (score)
 
score.remove(max(score))
score.remove(min(score))
 
result = sum(score) / len(score)
 
print (result)