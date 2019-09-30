# -*- coding: UTF-8 -*-

for i in range(4):
    for j in range(2 - i + 1):
        print(' ',end='')
    for k in range(2 * i + 1):
        print('*',end='')
    print()
 
for i in range(3):
    for j in range(i + 1):
        print(' ',end='')
    for k in range(4 - 2 * i + 1):
        print('*',end='')
    print()