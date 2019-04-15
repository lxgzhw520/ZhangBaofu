# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 21:13
# 文件名称: hw_007_类的打印和删除方法.py
# 开发工具: PyCharm

class Person:
    def __del__(self):
        print('实例被销毁的时候自动触发')

    def __str__(self):
        return '打印实例的时候自动触发'


lky = Person()  # 程序执行结束后,实例会被自动销毁
print(lky)
