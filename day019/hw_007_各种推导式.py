# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 11:39
# 文件名称: hw_007_各种推导式.py
# 开发工具: PyCharm

# 列表推导式
l = [i for i in range(10)]
print(l)

# 生成器推导式
l1 = (i for i in range(10))
print(l1)

# 集合推导式
l2 = {i for i in range(10)}
print(l2)
# 字典推导式
l3 = {'第%s个' % i: i for i in range(10)}
print(l3)
