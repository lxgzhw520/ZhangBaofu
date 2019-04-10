# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/7 17:05
# 文件名称: hw_002_正则表达式常用方法.py
# 开发工具: PyCharm
import re

pattern = re.compile(r'\d')
ret = pattern.findall('aaa111dddccc22sfas342dsfwqe4q312')
print(ret)

# re.sub()
# re.split()
