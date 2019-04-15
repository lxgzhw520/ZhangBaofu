# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 07:06
# 文件名称: hw_002_静态方法.py
# 开发工具: PyCharm

# java 只支持面向对象
class Login:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @staticmethod
    def login():
        name = input("请输入用户名:")
        password = input("请输入密码:")
        return Login(name, password)


l = Login.login()
print(l.name)
print(l.password)
