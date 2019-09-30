#coding:utf-8
 
# a:1-9, b:0-9, c:0-9
l = range(10)
count = 0
 
for a in l[1:]:
    for b in l:
        if a == b: continue #过滤a == b
        for c in l:
            if c != a and c != b: #过滤a == c, b == c
                print (a, b, c)
                count += 1
 
print ('count:', count)