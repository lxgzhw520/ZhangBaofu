# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 21:23
# 文件名称: hw_002_单例模式.py
# 开发工具: PyCharm

class Person:
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否为空对象
        if cls.instance is None:
            # 调用父类方法,为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 如果instance有值了,就直接返回
        # 这样能保证instance始终使用同一块内存
        # 也就是对象永远是同一个
        return cls.instance


# 回忆  id()方法测试一个变量的内存
p1 = Person()
p2 = Person()
p3 = Person()

print(id(p1), id(p2), id(p3))
# 判断内存地址是否相等
print(id(p1) == id(p2) == id(p3))
