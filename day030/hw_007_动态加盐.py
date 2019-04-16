# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 10:38
# 文件名称: hw_007_动态加盐.py
# 开发工具: PyCharm
# 动态加盐
# 用户名 密码
# 使用用户名的一部分或者 直接使用整个用户名作为盐
import hashlib  # 提供摘要算法的模块

md5 = hashlib.md5(bytes('加一些东西', encoding='utf-8') + b'')
# md5 = hashlib.md5()
md5.update(b'123456')
print(md5.hexdigest())
