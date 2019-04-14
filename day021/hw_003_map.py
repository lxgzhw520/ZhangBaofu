# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 06:32
# 文件名称: hw_003_map.py
# 开发工具: PyCharm

# map将一个函数映射到数组的每一个元素
print(map(lambda x: x ** 2, [-1, 2, 22, 33, -44]))

# map是可迭代对象,可以用for直接遍历
for i in map(lambda x: x ** 2, [-1, 2, 22, 33, -44]):
    print(i)
