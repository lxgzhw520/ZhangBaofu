# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/3/31 21:01
# 文件名称: hw_008_同时获取列表的元素和索引.py
# 开发工具: PyCharm
l = ['Google', 'Runoob', 'Taobao']

# 能够把一个列表 转换为 {索引:列表}
for index, item in enumerate(l):
    print('{}:{}'.format(index, item))
