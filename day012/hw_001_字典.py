# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 09:12
# 文件名称: hw_001_字典.py
# 开发工具: PyCharm

# 定义一个空字典
d = {}
# 定义一个带数据的字典
# 字典的键必须是不可变数据类型,一般是一个字符串
d1 = {'name': '李柯瑶'}
# 定义多个参数的字典
d2 = {
    'name': '李珂瑶',
    'age': 18,
    'gender': '女'
}
print('------------打印字典--------------\n')
print(d)
print(d1)
print(d2)

# 添加值 和list不一样,字典添加新值,不存在不会报错
d['country'] = '中国'
d1['country'] = '中国'
d2['country'] = '中国'

print('------------打印字典--------------\n')
print(d)
print(d1)
print(d2)
# 通过打印我们知道,数据都已经添加成功了

# 删除值 删除方法较多,一般用通用方法del即可
del d['country']
del d1['country']
del d2['country']
print('------------打印字典--------------\n')
print(d)
print(d1)
print(d2)

# 添加值 和list不一样,字典添加新值,不存在不会报错
d['country'] = '中国'
d1['country'] = '中国'
d2['country'] = '中国'

print('------------打印字典--------------\n')
print(d)
print(d1)
print(d2)
# 用pop删除
d.pop('country')
d1.pop('country')
d2.pop('country')
print('------------打印字典--------------\n')
print(d)
print(d1)
print(d2)

# 修改 直接赋值就行即可

d['country'] = '中国'
d1['country'] = '中国'
d2['country'] = '中国'

print('------------打印字典--------------\n')
print(d)
print(d1)
print(d2)
# 修改
d['country'] = '中国被修改了'
d1['country'] = '中国修改'
d2['country'] = '中国'
print('------------打印字典--------------\n')
print(d)
print(d1)
print(d2)
# 查询 可以用下标查询 但是最好用get
print('------------打印字典--------------\n')
print(d.get('country'))
print(d1.get('country'))
print(d2.get('country'))
