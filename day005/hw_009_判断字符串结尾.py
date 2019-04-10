# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/5 17:13
# 文件名称: hw_009_判断字符串结尾.py
# 开发工具: PyCharm

Str = 'Runoob example....wow!!!'
suffix = '!!'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 20))
suffix = 'run'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 0, 19))
