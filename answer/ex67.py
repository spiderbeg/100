# coding:utf8

def output(s,l):
    if l==0:
       return
    print(s[l-1])
    output(s,l-1)
 
s = input('Input a string:')
l = len(s)
output(s,l)