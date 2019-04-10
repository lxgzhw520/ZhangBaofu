# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/9 17:58
# 文件名称: hw_004_实战_正则匹配猫眼电影排行.py
# 开发工具: PyCharm

import requests
import re

html = requests.get('https://maoyan.com/board').text
# print(html)

# 第一步 得到电影列表
dd_list = re.findall(r'<dd>(.*?)</dd>', html, re.S)

# 第二步 遍历电影列表 提取每一步电影的信息
movies = []
for movie in dd_list:
    # print(movie)
    # 提取电影名称
    print(re.search(r'title="(.*?)"', movie, re.S).group(1))
    title = re.search(r'title="(.*?)"', movie, re.S).group(1)
    # 提取主演
    print(re.search(r'<p class="star">(.*?)</p>', movie, re.S).group(1).strip())
    role = re.search(r'<p class="star">(.*?)</p>', movie, re.S).group(1).strip()
    # 提取上映时间
    print(re.search(r'<p class="releasetime">(.*?)</p>', movie, re.S).group(1).strip())
    time = re.search(r'<p class="releasetime">(.*?)</p>', movie, re.S).group(1).strip()
    # 提取海报图片
    print(re.findall(r'src="(.*?)"', movie, re.S)[1])
    img = re.findall(r'src="(.*?)"', movie, re.S)[1]
    # exit()
    movies.append({
        'title': time,
        'role': role,
        'time': time,
        'img': img
    })

# 第三步 打印测试
for movie in movies:
    print(movie)
