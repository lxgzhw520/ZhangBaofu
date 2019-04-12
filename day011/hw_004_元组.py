# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 08:44
# 文件名称: hw_004_元组.py
# 开发工具: PyCharm

# 元组和列表类似 不过列表是用()定义的 值不可修改
t = ()  # 定义一个空元组
print(type(t))

t1 = (1,)  # 定义一个元素的列表
print(type(t1))  # type用来打印一个数据的类型
t2 = (1)  # 注意一个元素必须加逗号,否则不是元组类型
print(type(t2))

# 元组推导式  这种方法是不行的
t = (i for i in range(10) if i % 2 == 0)
print(t)
print(type(t))

# 要快速生成元组,需要先生成列表,再将列表转换为元组
# 注意这里的推导式 加了一个判断条件
# 格式[元素 元素取值  元素取值的过滤条件]
t = tuple([i for i in range(10) if i % 2 == 0])
print(t)
print(type(t))

# 适用于列表的方法,一般也适用于元组
print('--' * 22)
# 长度
print(len(t))
# 统计
print(t.count(2))
# 索引
print(t.index(2))
# 排序 是不可用的
# t.sort()
# 反转 也不可用
# t.reverse()

# 访问 用索引
print(t[1])
