# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 08:53
# 文件名称: hw_005_打印字符串每个元素.py
# 开发工具: PyCharm

# 任意输入一个字符串,使用while和for循环分别打印其中的每一个元素
s = input("请输入任意字符:")

# for 直接遍历
for i in s:
    print(i)
print('--' * 22)
# while 先得到长度,再以长度作为条件进行遍历
i = 0
while i < len(s):
    print(s[i])
    i += 1
