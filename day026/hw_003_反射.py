# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 22:14
# 文件名称: hw_003_反射.py
# 开发工具: PyCharm

class Teacher:
    dic = {'查看学生信息': 'show_student', '查看讲师信息': 'show_teacher'}

    def show_student(self):
        print('show_student')

    def show_teacher(self):
        print('show_teacher')

    @classmethod
    def func(cls):
        print('hahaha')


zbf = Teacher()
key = '查看学生信息'
# 第一个参数是对象,第二个参数是方法名
# hasattr判断有没有这个属性方法
# getattr获取这个属性方法并返回
if hasattr(zbf, Teacher.dic[key]):
    func = getattr(zbf, Teacher.dic[key])
    # 接收后可以直接调用
    func()
