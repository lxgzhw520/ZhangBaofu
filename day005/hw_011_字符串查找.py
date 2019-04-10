# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/5 17:15
# 文件名称: hw_011_字符串查找.py
# 开发工具: PyCharm

str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.find('e'))
print('------------------')
print(str1.find(str2))
print(str1.find(str2, 1))
print(str1.find(str2, 5))
print(str1.find(str2, 5, 11))
print(str1.find(str2, 7, 11))
print(str1.find(str2, 9, 11))
print(str1.find(str2, 10))
