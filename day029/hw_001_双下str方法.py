# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:32
# 文件名称: hw_001_双下str方法.py
# 开发工具: PyCharm


# 内置的类方法和内置的函数之间关系非常紧密

print(repr(1))
print(repr('1'))
print(1, '1')

print('--' * 22)


class A:
    def __str__(self):
        return 'A的说明信息:原生调用的是地址{}'.format(id(self))


a = A()
# 实际上是调用了类的 __str__方法
print(str(a))
print(a)


class B:
    def __str__(self):
        return "{}:{}".format('B', id(self))

    pass


b = B()
print(b)
