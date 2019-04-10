# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/7 17:07
# 文件名称: hw_003_匹配手机号.py
# 开发工具: PyCharm

s = '18822228888'
s1 = 'a18822228888'
s2 = 'a18822228888a'
s3 = 'a18822 228888a'
import re

pattern = re.compile(r'\d{11}')
print(pattern.findall(s))
print(pattern.findall(s1))
print(pattern.findall(s2))
print(pattern.findall(s3))
