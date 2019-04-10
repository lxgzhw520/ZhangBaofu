# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/7 21:09
# 文件名称: hw_004_匹配邮箱号.py
# 开发工具: PyCharm


# 要求 用户输入邮箱,然后判断,邮箱格式是否正确,再打印
s = input('请输入一个邮箱:')
import re

pattern = re.compile(r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]+$')

# 输出咱们的判断
result = pattern.findall(s)
# 什么类型 列表 空列表[]
# 怎么判断是不是真的呢
if result:
    print('这个邮箱格式是正确的')
else:
    print('邮箱格式不正确')
