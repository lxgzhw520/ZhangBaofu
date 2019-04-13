# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 08:47
# 文件名称: hw_002_写入文件.py
# 开发工具: PyCharm

f = open('README.md', mode='r+', encoding='utf8')

content = f.read()
# print(content)
content += '\n## 读取文件'
print(content)

# 写入文件
f.write(content)

f.close()
