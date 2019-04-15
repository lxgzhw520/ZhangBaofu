# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 07:27
# 文件名称: hw_003_反射.py
# 开发工具: PyCharm

# 反射 通过字符串拿到变量
class Teacher:
    dic = {
        '查看学生信息': 'show_student'
    }

    @staticmethod
    def show_student():
        print("这里是学生信息")
        print("这里是学生信息")
        print("这里是学生信息")
        print("这里是学生信息")
        print("这里是学生信息")


d = 'dic'
# 实现发射的机制(从哪里取,取什么)
print(getattr(Teacher, d))
res = getattr(Teacher, d)
print(res, type(res))
print(res.get('查看学生信息'))
res = getattr(Teacher, res.get('查看学生信息'))
print(res)
res()
