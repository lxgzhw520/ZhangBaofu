# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 10:15
# 文件名称: hw_004_用户登录和注册.py
# 开发工具: PyCharm

# 需求:实现用户的登录和注册功能
# 1 用户注册并将数据存入文件
# 2 用户登录并读取文件验证账号密码是否正确

# 分析 循环 功能选择 录入数据  存储数据 读取数据
info = """
1 登录系统
2 注册账号
3 退出系统
请选择功能(1/2/3):\t
"""
with open('password.csv', 'a+') as f:
    if not f.readlines():
        f.write("账号,密码\n")
    while True:
        print(info)
        if input() == '3':
            break
        if input() == '1':
            # 登录系统
            username = input('请输入用户名:')
            password = input("请输入密码:")
            # 读取csv并验证
            print(f.readlines())
        elif input() == '2':
            # 注册账号
            username = input('请输入用户名:')
            password = input("请输入密码:")
            if username and password:
                f.write('%s,%s\n' % (username, password))
                print('恭喜您,注册成功.')
            else:
                print('用户名或密码不能为空.')
        else:
            print('输入错误,请检查后重新输入.')
