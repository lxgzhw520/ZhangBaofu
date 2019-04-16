# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 06:14
# 文件名称: hw_001_日志复习.py
# 开发工具: PyCharm
# 导入
import logging

# 实例化
logger = logging.getLogger()
# 设置日志记录等级
logging.basicConfig(level=logging.INFO)
# 设置日志记录文件以及编码
fh = logging.FileHandler('log.log', encoding='utf-8')
# 设置日志的记录格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 将记录格式添加到记录文件对象
fh.setFormatter(formatter)
# 将记录文件对象添加到日志实例
logger.addHandler(fh)
