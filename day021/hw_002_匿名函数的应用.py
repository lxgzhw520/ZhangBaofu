# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 06:13
# 文件名称: hw_002_匿名函数的应用.py
# 开发工具: PyCharm

# 我需要得到字典中值最大的那个
dic = {
    'a': 10,
    'b': 20,
    'aaa': 33,
    'aab': 44
}


def func(k):
    return dic[k]


# max可以传入一个函数作为过滤条件
print(max(dic, key=func))
print(max(dic, key=lambda k: dic[k]))

# 根据绝对值,求一个数组中的最大值
print(max([1, -11, 22, -33, 44], key=abs))
# abs()用来求一个数的绝对值
print(abs(-33))
