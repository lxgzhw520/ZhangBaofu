# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 11:03
# 文件名称: hw_001_密码加密复习.py
# 开发工具: PyCharm

import hashlib

md5 = hashlib.md5(bytes('加一些东西', encoding='utf8') + b'aaa')

password = input("密码:")
md5.update(bytes(password, encoding='utf8'))
p1 = md5.hexdigest()
print(p1)

md5 = hashlib.md5(bytes('加一些东西', encoding='utf8') + b'aaa')
password = input("确认密码:")
md5.update(bytes(password, encoding='utf8'))
p2 = md5.hexdigest()
print(p2)

if p1 == p2:
    print('密码一致')
