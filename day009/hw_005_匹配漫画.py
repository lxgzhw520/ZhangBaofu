# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/9 17:58
# 文件名称: hw_004_实战_正则匹配猫眼电影排行.py
# 开发工具: PyCharm

import requests
import re

html = requests.get(
    'https://tieba.baidu.com/p/6086323678?fr=ala0&pstaala=1&tpl=5&fid=11772&isgod=0&red_tag=1584853091').text
# print(html)
import re

# print(re.findall(r'<img class="BDE_Image".*?src="(.*?)">', html, re.S))
# list = re.findall(r'<img class="BDE_Image".*?src="(.*?)">', html, re.S)
# ?
list = re.findall(r'<img class="BDE_Image".*?src="(.*?)".*?>', html)
# list = re.findall(r'<img class="BDE_Image".*?src="(.*?)" >', html)
for i in list:
    print(i)
