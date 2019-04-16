# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 10:41
# 文件名称: hw_008_密码加密保存.py
# 开发工具: PyCharm


import hashlib

# 输入密码
password = input("请输入密码:")
md5 = hashlib.md5(bytes('加一些东西', encoding='utf-8') + b'')
md5.update(bytes(password, encoding='utf8'))
print(md5.hexdigest())

# 确认密码
password = input("请输入密码:")
md5 = hashlib.md5(bytes('加一些东西', encoding='utf-8') + b'')
md5.update(bytes(password, encoding='utf8'))
print(md5.hexdigest())
