# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/3/31 20:37
# 文件名称: hw_018_列表删除.py
# 开发工具: PyCharm

list1 = ['physics', 'chemistry', 1997, 2000]

# 第一种方法是比较暴力的方法  而且是通用方法
# del  关键字 缩写  delete的缩写
# 非常暴力,非常彻底,非常通用的方法
# 不止能够删除列表元素 也能删除方法 删除类 删除几乎一切你想删除的东西
print(list1)
print(list1[1])
del list1[1]
print(list1)
# 删除 暂时记这一种方法就行
# pop  弹出来 把最后一个元素给弹出
list1.pop()
print(list1)
