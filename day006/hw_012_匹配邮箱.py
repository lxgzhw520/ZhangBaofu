# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 17:32
# 文件名称: hw_012_匹配邮箱.py
# 开发工具: PyCharm

s = 'lxg@lxg.com'
# 判断是否是邮箱
import re

print(re.findall(r'\w+@\w+\.\w+', s))
