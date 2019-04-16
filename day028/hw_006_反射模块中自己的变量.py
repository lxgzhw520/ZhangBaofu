# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:22
# 文件名称: hw_006_反射模块中自己的变量.py
# 开发工具: PyCharm

a = 'aaa自己模块'
import sys

# __main__ 表示当前模块
print(getattr(sys.modules['__main__'], 'a'))


def show():
    print("人生苦短,我用Python")


# 反射自己模块内的方法
getattr(sys.modules['__main__'], 'show')()
# __name__ 也表示当前模块
getattr(sys.modules[__name__], 'show')()
