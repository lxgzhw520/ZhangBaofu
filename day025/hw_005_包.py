# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 21:37
# 文件名称: hw_005_包.py
# 开发工具: PyCharm

# 包就是包含 __init__.py的文件夹
# 包里面装的一般都是各种Python类
# 导入我们自己写的包

# 方法1
from Students import Student

Student.Student.static_method()

# 方法2
from Students.Student import Student

lky = Student('李珂瑶', 18)
print(lky.name)
print(lky.age)
lky.show()
print('--' * 22)
lky = Student('张宝富', 33)
print(lky.name)
print(lky.age)
lky.show()
