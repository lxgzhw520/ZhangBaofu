# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 21:28
# 文件名称: hw_003_单例对象初始化.py
# 开发工具: PyCharm

class Person:
    instance = None
    start = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if Person.start:
            return
        print("单例对象被创建了")
        Person.start = True


# 通过控制台可以看到 初始化代码只执行了一次
# 这是我们通过start标记手动控制的
p1 = Person()
p2 = Person()
p3 = Person()
