# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 11:59
# 文件名称: hw_002_reversed.py
# 开发工具: PyCharm

l = [i for i in range(10)]
print(l)
# 得到的是一个迭代器 反转后的
l = reversed(l)
print(l)
for i in l:
    print(i, end='\t')

print()

# 字符串也可以反转
s = 'hello world'
s = reversed(s)
print(s)
for i in s:
    print(i, end='\t')
