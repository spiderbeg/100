# coding:utf8
# a:(1-9), b:(0-9), c:(1-9)
# a != b != c
# a < c
for b in range(10):
    for a in range(1, 10):
        if a == b: continue
        for c in range(a + 1, 10):
            if c == b: continue
            t1 = 100 * a + 10 * b + c
            t2 = 100 * c + 10 * b + a
            if t1 * t2 == 280021: 
                print(t1, t2)