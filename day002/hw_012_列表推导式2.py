# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/3/31 21:08
# 文件名称: hw_012_列表推导式.py
# 开发工具: PyCharm

for i in range(1, 10, 2):
    print(i, end='\t')
print()
# 第一种
l = [i for i in range(1, 10, 2)]
print(l)

# 求1-100之间所有数之和
print(sum([i for i in range(101)]))
