# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 12:02
# 文件名称: hw_003_bytes.py
# 开发工具: PyCharm


# 转换为字符编码
print(bytes('hello你好', encoding='utf8'))
s = bytes('hello你好', encoding='utf8')

# 解码
print(s.decode('utf8'))

# 另一种方式
s = '中国文字aaaa'
print(s)
s = s.encode('utf8')
print(s)
print(s.decode('utf8'))
