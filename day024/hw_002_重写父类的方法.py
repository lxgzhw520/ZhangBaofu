# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 20:48
# 文件名称: hw_002_重写父类的方法.py
# 开发工具: PyCharm

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 父类方法
    def show(self):
        print("我是一个人类")


# 继承父类 不重写方法
class Student1(Person):
    pass


# 继承父类 重写方法
class Student2(Person):
    def show(self):
        print("我是{}".format(self.name))


lky = Student1('李珂瑶', 18)
print(lky.name)
print(lky.age)
# 使用的是父类的方法
lky.show()  # 我是一个人类
print('--' * 22)
lky = Student2('李珂瑶', 18)
print(lky.name)
print(lky.age)
lky.show()
