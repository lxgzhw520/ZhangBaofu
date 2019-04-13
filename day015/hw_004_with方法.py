# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 08:53
# 文件名称: hw_004_with方法.py
# 开发工具: PyCharm

# with方法会帮我们自动关闭文件
with open('README.md', mode='r+', encoding='utf8') as f:
    content = f.read()
    print(content)
    # 写入
    content += '\n- with方法会帮我们自动关闭文件,建议用'
    f.write(content)
    print('写入成功')
