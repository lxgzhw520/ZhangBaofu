# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 17:30
# 文件名称: hw_011_匹配手机号.py
# 开发工具: PyCharm

s = '18811118888'
# 解决这个
s1 = '00000000000'
# 解决这个
s2 = '10000000000'

import re

pattern = re.compile(r'^1[3578]\d{9}$')
#拆
# pattern = re.compile(r'^13\d{9}$')
# pattern = re.compile(r'^15\d{9}$')
# pattern = re.compile(r'^17\d{9}$')
print(pattern.findall(s))
print(pattern.findall(s1))
print(pattern.findall(s2))
