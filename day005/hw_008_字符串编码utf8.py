# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/5 17:12
# 文件名称: hw_008_字符串编码.py
# 开发工具: PyCharm

str = "理想国真恵玩"
# 编码 encode
# 解码 decode

s = str.encode('utf8')
print(s)
print(s.decode('utf8'))

s = str.encode('utf-8')
print(s)
print(s.decode('utf-8'))

s = str.encode('utf-8')
print(s)
print(s.decode('utf8'))
