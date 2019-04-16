# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:08
# 文件名称: hw_003_反射.py
# 开发工具: PyCharm


# 反射安全性很高
# 反射对象中的属性和方法
class A:
    def func(self):
        print('是方法')


a = A()
a.name = '张宝富'

# 反射的四个方法 hasattr getattr setattr delattr

# 反射对象的属性
ret = getattr(a, 'name')
print(ret)

# 反射对象的方法
f = 'func'
ret = getattr(a, f)
ret()
