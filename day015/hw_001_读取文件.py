# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 08:43
# 文件名称: hw_001_读取文件.py
# 开发工具: PyCharm

# 文件操作必不可少的两步 打开和关闭

# 打开
f = open('README.md', mode='r', encoding='utf8')
# 操作
content = f.read()
print(content)

# 关闭
f.close()
