# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 17:16
# 文件名称: hw_009_匹配开头.py
# 开发工具: PyCharm

# ^	匹配字符串的开头
import re

print(re.findall(r'^a', 'a,ba,ab,abc,aa'))
print(re.findall(r'^a', 'a ba ab abc aa'))

pattern = re.compile('^a')
print(pattern.findall('a,ba,ab,abc,aa'))
