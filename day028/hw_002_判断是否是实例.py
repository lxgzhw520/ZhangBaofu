# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:07
# 文件名称: hw_002_判断是否是实例.py
# 开发工具: PyCharm

class A:
    pass


a = A()

# a的类是不是A
print(isinstance(a, A))
