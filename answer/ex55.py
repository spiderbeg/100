# -*- coding: UTF-8 -*-

count = 0 
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                count+=1
                print(i,j,k)
print('共 %d 种组合'%count)