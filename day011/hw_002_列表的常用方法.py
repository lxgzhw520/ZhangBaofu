# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 08:34
# 文件名称: hw_002_列表的常用方法.py
# 开发工具: PyCharm

# 快速的得到一个新的列表  列表推导式
# 格式: [列表的元素  元素的获取方法]
l = [i for i in range(10)]
print(l)

# 列表的长度
print(len(l))

# 统计某元素的数量
print(l.count(1))

# 排序会直接修改列表的结构,而不是返回值
# 正向排序
l.sort()
print(l)

# 反向排序
l.sort(reverse=True)
print(l)
# 获取指定值的下标
print(l.index(3))
# 反转
l.reverse()
print(l)

# 插入  insert(位置,值)
l.insert(0, '第一个位置插入')
print(l)
l.insert(-1, "最后一个位置插入")  # 注意是插在倒数第一个
print(l)
# 实现插在最后一个直接用追加
l.append("实现最后一个位置插入")
print(l)

# 删除最后一个数
l.pop()
print(l)

# 删除指定位置的数
print("要被删除的数:", l[-2])
del l[-2]
print(l)
