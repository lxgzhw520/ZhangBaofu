# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 11:07
# 文件名称: hw_002_类的成员变量.py
# 开发工具: PyCharm

# 定义在__init__方法中的叫做成员变量

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建的时候动态赋值
lky = Person('李珂瑶', 18)
# 调用直接用点方法
print(lky.name)
print(lky.age)
