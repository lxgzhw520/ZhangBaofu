# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 09:40
# 文件名称: hw_002_双下new方法.py
# 开发工具: PyCharm

# __init__初始化方法
# __new__构造方法 创建一个对象

class A:
    __instance = False

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print("创建新对象的时候自动执行")
        if cls.__instance:
            return cls.__instance
        cls.__instance = object.__new__(A)
        return cls.__instance


# a = A()
# 设计模式 23种
# 单例模式:一个类始终只有一个实例
# 当你第一次实例化这个类的时候,就创建一个实例化的对象
# 当你之后再来实例化的时候,就用之前创建的对象

zbf = A('张宝富', 33)
# 值取代了之前的赋值 但是内存地址还是同一个
lky = A('李珂瑶', 18)
print('--' * 22)
print(zbf.name, zbf.age)
print(lky.name, lky.age)
print('--' * 22)
print(id(zbf))
print(id(lky))
print(id(lky) == id(zbf))
