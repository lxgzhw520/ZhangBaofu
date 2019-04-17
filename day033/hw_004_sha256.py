# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 09:07
# 文件名称: hw_004_sha256.py
# 开发工具: PyCharm
import hashlib

sha256 = hashlib.sha256(bytes('加一些东西', encoding='utf8') + b'lxgzhw')
password = input("请输入密码:")
sha256.update(bytes(password, encoding='utf8'))
p1 = sha256.hexdigest()
print(p1)

sha256 = hashlib.sha256(bytes('加一些东西', encoding='utf8') + b'lxgzhw')
password = input("请输入密码:")
sha256.update(bytes(password, encoding='utf8'))
p2 = sha256.hexdigest()
print(p2)

if p1 == p2:
    print("密码一致")
