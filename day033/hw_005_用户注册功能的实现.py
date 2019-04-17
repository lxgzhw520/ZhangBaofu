# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 09:12
# 文件名称: hw_005_用户注册功能的实现.py
# 开发工具: PyCharm

# 需要,用户输入账号密码,确认提交后验证,无误则保存到users.csv
# 依赖
import os  # 文件操作
import hashlib  # 密码加密

# 先创建自定义的数据库
if not os.path.exists('users.csv'):
    with open('users.csv', 'w') as f:
        f.write('用户名,密码\n')
# 让用户输入账号密码
username = input("请输入用户名:")
password = input("请输入密码:")
password1 = input("请确认密码:")
if username and password and password == password1:
    print("验证成功")
    sha256 = hashlib.sha256(bytes('加一些东西', encoding='utf8') + b'lxgzhw')
    sha256.update(bytes(password, encoding='utf8'))
    password = sha256.hexdigest()
    print(password)

# 存储数据库
is_exist = False
# 确认该用户不存在
with open('users.csv', 'r') as f:
    for i in f:
        if username in i:
            print(i)
            is_exist = True
if is_exist:
    print("该用户已存在")
else:
    # 不存在则保存到数据库
    with open('users.csv', 'a') as f:
        f.write('%s,%s\n' % (username, password))
    print("恭喜,用户注册成功,现在您可以登录了.")
