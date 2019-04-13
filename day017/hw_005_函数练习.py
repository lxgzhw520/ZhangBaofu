# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 07:09
# 文件名称: hw_005_函数练习.py
# 开发工具: PyCharm

# 定义一个函数,传入一个列表,返回列表中的最大值,最小值,平均值
def show_list(l):
    # 系统提供的方法  max最大值 min最小值 sum求和
    return max(l), min(l), sum(l) / len(l)


result = show_list([i for i in range(100)])

print(result)


# 定义一个函数,过滤掉 敏感词1 敏感词2
def filter_string(s):
    l = ['敏感词1', '敏感词2']
    for i in l:
        s = s.replace(i, '*')
    return s


print(filter_string('敏感词1.粉丝佛诶无肉我就饿哦跑任务敏感词29i09i0923i049i2349'))
