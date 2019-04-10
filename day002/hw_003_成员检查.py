# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/3/31 20:53
# 文件名称: hw_003_成员检查.py
# 开发工具: PyCharm

list1 = ['physics', 'chemistry', 1997, 2000]
print('physics' in list1)

# 包含不包含 在不在列表里面
# 返回值 True False
# 布尔
# 布尔有什么特点
# 布尔只有两个值:要么真,要么假
# 通常 哪些表达式(代码执行)  会得到一个布尔值
# 比较 成员运算符 得到就是布尔值 in
# not in


a = [1, 2, 3, 4, 5, 6, 8, 999]

# 两个问题
# 1 在这个列表中吗
print(1 in a)
# 完善的 for遍历
# try
if 1 in a:
    print('1 在列表中')
else:
    print('1 不在列表中')
# 11 在这个列表中吗
if 11 in a:
    print('11 在列表中')
else:
    print('11 不在列表中')
