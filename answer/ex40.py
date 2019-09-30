# encoding:utf8
test_str = "Crossin 的编程教室"
 
# 输出原始字符串
print ("原始字符串为 : " + test_str)
 
# 移除第8个字符 空白符
new_str = ""
 
for i in range(0, len(test_str)):
    if i != 7:
        new_str = new_str + test_str[i]

print ("字符串移除后为 : " + new_str)