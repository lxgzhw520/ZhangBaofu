# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 11:14
# 文件名称: hw_005_成员方法.py
# 开发工具: PyCharm

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 成员方法就是第一个参数是self的方法
    def show(self):
        print("名字:{}\n年龄:{}\n".format(self.name, self.age))


lky = Person("李珂瑶", 18)
zbf = Person("张宝富", 33)
lky.show()
zbf.show()
