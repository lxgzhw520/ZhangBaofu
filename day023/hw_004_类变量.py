# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 11:12
# 文件名称: hw_004_类变量.py
# 开发工具: PyCharm

# 类变量就是写在class下面而不是init里面的变量
class Person:
    name = None
    age = None


# 调用用法一样
lky = Person()
lky.name = '李珂瑶'
lky.age = 18
print(lky.name)
print(lky.age)

# 区别是,不实例化也可以使用类变量
print(Person.name)
Person.name = '张宝富'
print(Person.name)
