# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/3 21:21
# 文件名称: hw_004_删除元组.py
# 开发工具: PyCharm

tup = ('Google', 'Runoob', 1997, 2000)

print(tup)
# del tup
print("删除后的元组 tup : ")
print(tup)

# 创建和修改的区别
# 不管是元组,还是字符串  "修改" 实际上是创建新的


# 删除某个元素
print(tup)
# del tup[1]
print(tup)
# 'tuple' object doesn't support item deletion
# 元组对象 不能支持 删除 元素
# 不可以被修改
