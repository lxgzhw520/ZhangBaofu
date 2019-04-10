# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 17:01
# 文件名称: hw_002_search.py
# 开发工具: PyCharm

# re.search 扫描整个字符串并返回第一个成功的匹配。
import re

# match 查找 有就返回真的
print(re.search('hello', 'helloworld  '))
print(re.search('hello', 'helloworld  ').span())
print(re.search('hello', 'aaa,bbb,ccc,hello').span())
print(re.search('hello', 'aaa,bbb,ccchello').span())
