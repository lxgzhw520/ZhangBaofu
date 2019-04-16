# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:17
# 文件名称: hw_005_反射模块的方法和属性.py
# 开发工具: PyCharm

from Person import Person

p = Person()
# 判断是否能够反射
print(hasattr(p, 'a'))
print(hasattr(p, 'b'))
print(hasattr(p, 'name'))

# 进行反射
print(getattr(p, 'b'))
getattr(p, 'a')()
print(getattr(p, 'name'))
