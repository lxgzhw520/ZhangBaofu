# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 17:34
# 文件名称: hw_013_匹配链接.py
# 开发工具: PyCharm

s = """
<a id="imsg" href="http://www.baidu.com/#" onmousedown="return user_c({'fm':'set','tab':'imsg','login':'1'})">消息</a>
"""
import re

# * 匹配0个或多个的表达式
# ? 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
print(re.findall(r'<a[\s\S]*?href="([\s\S]*?)"[\s\S]*?</a>', s))
