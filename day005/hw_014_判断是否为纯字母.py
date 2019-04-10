# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/5 17:19
# 文件名称: hw_014_判断是否为纯字母.py
# 开发工具: PyCharm

str = "runoob"
print(str.isalpha())
# 只能是字母 不能保护字母,空格,符号等其他任何元素
str = "Runoob example....wow!!!"
print(str.isalpha())

print('111'.isalpha())
print('111aaa'.isalpha())
