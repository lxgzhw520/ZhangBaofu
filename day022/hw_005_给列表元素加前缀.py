# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 07:32
# 文件名称: hw_005_给列表元素加前缀.py
# 开发工具: PyCharm

l = ['aaa', 'bbb', 'ccc']
# 需求 给每个元素加上 lxg_的前缀
# 分析:用map

ret = map(lambda x: 'lxg_%s' % x, l)
print(list(ret))

# 一行代码实现
print(list(map(lambda x: 'lxg_%s' % x, l)))
