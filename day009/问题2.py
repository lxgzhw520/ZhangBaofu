# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/9 17:58
# 文件名称: hw_004_实战_正则匹配猫眼电影排行.py
# 开发工具: PyCharm

import requests

html = requests.get('https://maoyan.com/board').text
# print(html) 整个网页源码
# 从网页中 提取排名

# <i></i>
import re

# print(re.findall(r'<i.*?>(\d+)</i>', html, re.S))
print(re.findall(r'<i.*?board-index-(\d+)>\d+</i>', html, re.S))
# 先找到电影所在的模块
