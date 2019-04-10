# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/3/31 21:08
# 文件名称: hw_012_列表推导式.py
# 开发工具: PyCharm

l = [i for i in range(10)]
print(l)

# 列表推导式
# range() 范围
for i in range(10):
    print(i)
# range(1)
for i in range(1):
    print(i)
# range(1,10)
# 编程中 PHP  java Python JavaScript C# .... 基本上 只要是带范围的
# 左包 右 不包
# 凡是索引 只要不是中国人发明的,基本都是从0开始的
for i in range(1, 10):
    print(i)
# range(1,10,2)
for i in range(1, 10, 2):
    print(i, end='\t')
print()
for i in range(1, 11, 2):
    print(i, end='\t')
print()
for i in range(1, 12, 2):
    print(i, end='\t')

# range(开始索引,结束索引,步长) range是一个序列一定是连着的
# 默认从0开始
