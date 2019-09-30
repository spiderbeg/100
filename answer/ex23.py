# encoding:utf8

a = input('请输入任意字符')
c = 0
for i in a:
    if 'b' == i:
        c+=1
print('字符 %s 中含 %d 个 "b".'%(a,c))
