# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 06:11
# 文件名称: hw_001_匿名函数.py
# 开发工具: PyCharm

def add1(x, y):
    return x + y


# 这种用lambda声明的就叫匿名函数
add2 = lambda x, y: x + y

print(add1(11, 22))
print(add2(11, 22))
