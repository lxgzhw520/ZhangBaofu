# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/7 17:09
# 文件名称: hw_004_匹配图片地址.py
# 开发工具: PyCharm

url = 'http://desk.zol.com.cn/bizhi/7490_92807_2.html'

s = """
<img id="bigImg" src="https://desk-fd.zol-img.com.cn/t_s960x600c5/g2/M00/0B/0F/ChMlWlyAyI-IN6eeAAva1cdvUO0AAIp0ADpDIQAC9rt777.jpg" width="960" height="600">
<img id="bigImg" src="https://desk-fd.zol-img.com.cn/t_s960x600c5/g2/M00/0B/0F/ChMlWlyAyI-IN6eeAAva1cdvUO0AAIp0ADpDIQAC9rt777.jpg" width="960" height="600">
<img id="bigImg" src="https://desk-fd.zol-img.com.cn/t_s960x600c5/g2/M00/0B/0F/ChMlWlyAyI-IN6eeAAva1cdvUO0AAIp0ADpDIQAC9rt777.jpg" width="960" height="600">
<img id="bigImg" src="https://desk-fd.zol-img.com.cn/t_s960x600c5/g2/M00/0B/0F/ChMlWlyAyI-IN6eeAAva1cdvUO0AAIp0ADpDIQAC9rt777.jpg" width="960" height="600">
<img id="bigImg" src="https://desk-fd.zol-img.com.cn/t_s960x600c5/g2/M00/0B/0F/ChMlWlyAyI-IN6eeAAva1cdvUO0AAIp0ADpDIQAC9rt777.jpg" width="960" height="600">
<img id="bigImg" src="https://desk-fd.zol-img.com.cn/t_s960x600c5/g2/M00/0B/0F/ChMlWlyAyI-IN6eeAAva1cdvUO0AAIp0ADpDIQAC9rt777.jpg" width="960" height="600">
"""
# https://desk-fd.zol-img.com.cn/t_s960x600c5/g2/M00/0B/0F/ChMlWlyAyI-IN6eeAAva1cdvUO0AAIp0ADpDIQAC9rt777.jpg
# 用正则表达式 把这个图片给匹配出来
import re

pattern = re.compile(r'http.*\.jpg')
print(pattern.findall(s))
for img in pattern.findall(s):
    print(img)
