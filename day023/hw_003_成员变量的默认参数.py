# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 11:09
# 文件名称: hw_003_成员变量的默认参数.py
# 开发工具: PyCharm

class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


# 当设置了默认参数以后,可以先实例化,后赋值
lky = Person()
lky.name = '李珂瑶'
lky.age = 18
print(lky.name)
print(lky.age)

# 也可以在创建的时候动态赋值
zbf = Person("张宝富", 33)
print(zbf.name)
print(zbf.age)
