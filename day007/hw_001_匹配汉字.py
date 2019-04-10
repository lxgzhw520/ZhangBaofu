# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/7 17:05
# 文件名称: hw_001_正则表达式常用符号.py
# 开发工具: PyCharm

# \w

s = "aaabbb啊啊啊啊啊xxx"

import re

# 可以匹配汉字
pattern = re.compile(r'\w')
print(pattern.findall(s))
