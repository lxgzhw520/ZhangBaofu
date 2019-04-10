# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/5 17:18
# 文件名称: hw_013_判断是否为字母加数字.py
# 开发工具: PyCharm
print('111'.isnumeric())
print('111'.isdigit())
print('111.00'.isdigit())
# 这个要注意
print('111'.isdecimal())
print('111.00'.isdecimal())

print('aaa222aaa'.isalnum())
print('aaa'.isalpha())
