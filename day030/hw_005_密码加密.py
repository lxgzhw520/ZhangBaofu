# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 10:23
# 文件名称: hw_005_密码加密.py
# 开发工具: PyCharm

import hashlib

password = input("请输入密码:")
# 第一次密码转换为md5
md5 = hashlib.md5()
# 注意 需要用byte格式的数据,bytes()方法必须传编码格式
md5.update(bytes(password, encoding='utf8'))
p = md5.hexdigest()
print(p)

# 第二次密码转换为hash值
password1 = input("确认密码:")
md5 = hashlib.md5()
md5.update(bytes(password1, encoding='utf8'))
p1 = md5.hexdigest()
print('--' * 22)
print(p1)
print(p)

# 验证密码是否项目
if password == password1:
    print('密码一致')

if p == p1:
    print("密码哈希值一致")
else:
    print("密码哈希值不一致")
