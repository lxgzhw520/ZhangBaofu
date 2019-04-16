# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:05
# 文件名称: hw_001_判断是否是子类.py
# 开发工具: PyCharm

class A:
    pass


class B(A):
    pass


# B的父类是不是A
print(issubclass(B, A))
print(issubclass(A, B))
