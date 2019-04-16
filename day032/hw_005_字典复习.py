# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 06:40
# 文件名称: hw_005_字典复习.py
# 开发工具: PyCharm
from random import randint
import logging

logger = logging.getLogger(name="张大鹏")
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
d = [{"name": "张宝富 %s" % i, 'age': randint(20, 40)} for i in range(100)]
logging.info(d)

# 遍历键
for i in d:
    for j in i.keys():
        logging.info(j)

    # 遍历值
    for j in i.values():
        logging.info(j)
    # 遍历项
    for j in i.items():
        logging.info(j)
