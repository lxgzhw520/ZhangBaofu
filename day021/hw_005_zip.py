# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 06:36
# 文件名称: hw_005_zip.py
# 开发工具: PyCharm

# zip用于将两个可迭代对象缝合起来
for i in zip((('a'), ('b')), (('a1'), ('b1'))):
    print(i)

# 缝合后的对象是元组
for i in zip([1, 2, 3], [-1, -2, -3]):
    print(i)

# 拼接字典的时候,只会把键拼接,
for i in zip({'name': 'aaa'}, {'age': 'bbb'}):
    print(i)
# 如果一定要拼接,可以使用字典的原生方法 指定键值对
for i in zip({'name': 'aaa'}.keys(), {'age': 'bbb'}.values()):
    print(i)
