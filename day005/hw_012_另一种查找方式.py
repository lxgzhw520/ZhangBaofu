# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/5 17:17
# 文件名称: hw_012_另一种查找方式.py
# 开发工具: PyCharm

str1 = "Runoob example....wow!!!"
str2 = "exam"

print(str1.index(str2))
print(str1.index(str2, 5))
# 找不到会报错
print(str1.index(str2, 10))
