# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 10:37
# 文件名称: hw_006_md5加盐.py
# 开发工具: PyCharm

import hashlib  # 提供摘要算法的模块

md5 = hashlib.md5(bytes('随便添加一些东西', encoding='utf-8'))
md5.update(b'123456')
print(md5.hexdigest())
