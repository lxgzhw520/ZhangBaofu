# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 11:11
# 文件名称: hw_002_日志.py
# 开发工具: PyCharm

# 日志 用来记录用户行为,或者diam的执行过程
# logging
# 错误,警告,消息
import logging

logging.debug('debug message')  # 低级别的 # 排错信息
logging.info('info message')  # 正常信息
logging.warning('warning message')  # 警告信息
logging.error('error message')  # 错误信息
logging.critical('critical message')  # 高级别的 # 严重错误信息

#配置 basicconfig 简单
#配置log对象