# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 17:30
# 文件名称: hw_011_匹配手机号.py
# 开发工具: PyCharm

s = '18811118888'
# 总共是11位 最简单方法
s1 = 'd18811118888'
s2 = '18811118888d'
s3 = '1881111 8888'
# 判断是否是手机号
import re

pattern = re.compile(r'^\d{11}$')
# ['18811118888'] 有返回结果 就说明匹配到了
print('s', pattern.findall(s))
print('s1', pattern.findall(s1))
print('s2', pattern.findall(s2))
print('s3', pattern.findall(s3))
