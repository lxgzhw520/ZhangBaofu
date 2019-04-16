# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 06:36
# 文件名称: hw_004_列表复习.py
# 开发工具: PyCharm
import logging

logger = logging.getLogger(name="张大鹏")
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
print('--' * 22)
from random import randint

l = [randint(-1000, 1000) for i in range(100)]
logging.info(l)
# 删除最一个后
l.pop()
# 删除第一个
del l[0]
# 删除前面五十个
del l[:50]
# 删除从第三个到最后一个
del l[3:]
logging.info(l)
