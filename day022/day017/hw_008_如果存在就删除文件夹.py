# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 10:28
# 文件名称: hw_008_如果存在就删除文件夹.py
# 开发工具: PyCharm

import os

if os.path.exists('test'):
    # 只有空文件夹才可以删除,判断是否为空文件夹
    if os.listdir('test'):
        # 删除非空文件夹
        import shutil

        shutil.rmtree('test')
    else:
        os.rmdir('test')
if os.path.exists('lxgPyWeb'):
    # 只有空文件夹才可以删除,判断是否为空文件夹
    if os.listdir('lxgPyWeb'):
        # 删除非空文件夹
        import shutil

        shutil.rmtree('lxgPyWeb')
    else:
        os.rmdir('lxgPyWeb')
