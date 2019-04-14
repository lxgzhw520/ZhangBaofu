# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 07:06
# 文件名称: hw_004_二分查找算法.py
# 开发工具: PyCharm

# 需求:生成一个随机数列表,用二分查找算法查找目标值
# 二分查找:每次将列表分为两半,找中间的值
# 生活案例:猜数字小游戏,一般猜最中间的

# 步骤
# 1 生成随机数列表 1000个元素
from random import randint

l = [randint(-1000, 1000) for i in range(1000)]
print(l)
print(len(l))
l.sort()


# 2 定义二分查找方法 这种方法只适用于排序后的列表
def find(l, aim, start=0, end=None):
    # 先对列表进行排序 确保从小到大,不会找错
    # l.sort()
    # 结束索引
    end = len(l) if end is None else end
    # 中间索引 +start确保每次都能找到目标列表的中间值
    mid_index = (end - start) // 2 + start
    # 如果开始索引小于等于结束索引 还可以继续找
    if start <= end:
        if l[mid_index] < aim:
            # 小于目标值 去右边找
            return find(l, aim, start=mid_index + 1, end=end)
        elif l[mid_index] > aim:
            # 大于目标值 去左边找
            return find(l, aim, start=start, end=mid_index - 1)
        else:
            # 等于目标值 找到了
            print("这个值的索引是:%d,值为:%d" % (mid_index, l[mid_index]))
            return mid_index
    else:
        return '找不到这个值'


# 3 使用二分查找方法查找目标值并打印
print(find(l, 66))
# print(l[find(l, 66)])
