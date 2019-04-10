# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/3/31 21:11
# 文件名称: hw_014_列表插入.py
# 开发工具: PyCharm

aList = [123, 'xyz', 'zara', 'abc']

# 向指定位置插入
aList.insert(3, 2009)
print(aList)

names = ['aaa', 'ccc']
# bbb 插入到中间
print(names)

# insert(索引, 值)
names.insert(1, 'bbb')
print(names)
# 这种需求很少
