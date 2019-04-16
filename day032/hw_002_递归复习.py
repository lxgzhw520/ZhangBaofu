# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 06:16
# 文件名称: hw_002_递归复习.py
# 开发工具: PyCharm
import logging

logger = logging.getLogger('张大鹏')
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


# 递归就是自己调用自己
def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n - 1)


for i in range(1, 11):
    logging.info(f(i))
