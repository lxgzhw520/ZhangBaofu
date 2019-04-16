# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 11:41
# 文件名称: hw_008_递归复习.py
# 开发工具: PyCharm
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


# 递归求阶乘
def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n - 1)


logging.info(fac(1))
logging.info(fac(2))
logging.info(fac(3))
logging.info(fac(4))
logging.info(fac(5))
logging.info(fac(6))
