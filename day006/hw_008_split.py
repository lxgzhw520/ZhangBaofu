# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 17:12
# 文件名称: hw_008_split.py
# 开发工具: PyCharm

# split 方法按照能够匹配的子串将字符串分割后返回列表
import re

# print(re.split('11', '2211223114441112341'))
# 分割


s = '1,2,3,4,5'
print(s.split(','))

# 下面这个更灵活 可以使用正则表达式
# print(re.split(',', s))
#
# s = '123aaa2aaa3ccc3423423cbbbb'
# print(re.split('\d', s))
l = ['', '', '', 'aaa', 'aaa', 'ccc', '', '', '', '', '', '', 'cbbbb']
new_l = []
for i in l:
    if len(i) <= 0:
        pass
    else:
        new_l.append(i)
print(new_l)
