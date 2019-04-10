# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/3/31 21:09
# 文件名称: hw_013_列表拓展.py
# 开发工具: PyCharm

aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)
print(aList)

# 效果一样
print('-----------------------------')
a = [123, 'xyz', 'zara', 'abc', 123]
b = [2009, 'manni']
a += b
print(a)
