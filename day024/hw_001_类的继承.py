# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 20:46
# 文件名称: hw_001_类的继承.py
# 开发工具: PyCharm

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 继承只需要加括号,括号里面写被继承的父类即可
# 继承的类用于父类的所有方法和属性
class Student(Person):
    pass


lky = Student('李珂瑶', 18)
print(lky.name)
print(lky.age)
