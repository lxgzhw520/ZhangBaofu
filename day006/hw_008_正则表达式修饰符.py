# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 17:13
# 文件名称: hw_008_正则表达式修饰符.py
# 开发工具: PyCharm
# re.I	使匹配对大小写不敏感
import re

print(re.findall('a', 'abcABCaAbBcC', re.I))
