# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 11:03
# 文件名称: hw_001_创建一个类.py
# 开发工具: PyCharm

# 定义一个类
class Person():
    # 这个方法负责接收类的参数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self的意思是自己
    # 这里定义类的方法
    def show(self):
        # 使用类的变量用 self.变量名
        print("姓名:{}\n年龄:{}\n".format(self.name, self.age))


LiKeyao = Person("李珂瑶", 18)
LiKeyao.show()


# 当不用继承的时候,可以不加括号
class Person:
    # 这个方法负责接收类的参数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self的意思是自己
    # 这里定义类的方法
    def show(self):
        # 使用类的变量用 self.变量名
        print("姓名:{}\n年龄:{}\n".format(self.name, self.age))


LiKeyao = Person("李珂瑶", 18)
LiKeyao.show()
