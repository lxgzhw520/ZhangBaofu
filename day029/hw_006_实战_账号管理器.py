# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 09:01
# 文件名称: hw_006_实战_账号管理器.py
# 开发工具: PyCharm

# 需求:定义一个类,用来管理用户的账号和密码以及id
# 要求id自增

class Users:
    count = 0
    users = []  # 用一个数组模拟数据库

    def __init__(self, name, password):
        Users.count += 1
        self.__id = Users.count  # 实现id自增
        # 将账号密码保护起来,不可直接调用
        self.__name = name
        self.__password = password

    # 注册方法
    @staticmethod
    def register():
        name = input("请输入用户名:")
        password = input("请输入密码:")
        if name and password:
            # 如果账号密码不为空,返回一个新用户
            # 存入数据库
            Users.users.append({
                'name': name,
                'password': password
            })
            return Users(name, password)

    # 登录方法
    @staticmethod
    def login():
        name = input("请输入用户名:")
        password = input("请输入密码:")
        if name and password:
            # 如果账号密码不为空,验证账号密码是否正确
            for i in Users.users:
                if i['name'] == name \
                        and i['password'] == password:
                    print("欢迎您,{},您已登录成功".format(name))
                    break


zbf = Users.register()
print('--' * 22)
Users.login()
