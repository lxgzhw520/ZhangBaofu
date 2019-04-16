# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 11:45
# 文件名称: hw_010_杨辉三角复习.py
# 开发工具:

import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def yh(n):
    if n <= 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        new_list = [1]
        for i in range(len(yh(n - 1)) - 1):
            new_list.append(yh(n - 1)[i] + yh(n - 1)[i + 1])
        new_list.append(1)
        return new_list


logging.info(yh(3))
logging.info(yh(4))
logging.info(yh(5))
logging.info(yh(6))
logging.info(yh(7))
logging.info(yh(8))
