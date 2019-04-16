# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:26
# 文件名称: hw_007_反射一个类.py
# 开发工具: PyCharm

import Person

# 查看能否反射
print(hasattr(Person, 'Person'))

# 进行反射
P = getattr(Person, 'Person')
# 查看类型
print(type(P))
p = P()
print(type(P))
# 设置类的属性
p.name = 'aaa'
print(p.name)
# 调用类的方法
p.a()
