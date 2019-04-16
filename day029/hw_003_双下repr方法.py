# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:40
# 文件名称: hw_003_双下repr方法.py
# 开发工具: PyCharm

class Person:
    def __repr__(self):
        return "%r自动调用"


p = Person()
print("%r" % p)

# 当没有重写__str__方法的时候,打印的时候会自动调用__repr__方法
print(p)
print('--' * 22)
r = repr(p)
print(r)
