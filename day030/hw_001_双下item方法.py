# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 09:31
# 文件名称: hw_001_双下item方法.py
# 开发工具: PyCharm

class A:
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]
        print("删除成功")


zbf = A('张宝富')
# 可以通过字典形式访问
print(zbf['name'])
# 赋值
zbf['age'] = 33
print(zbf['age'])
del zbf['age']
