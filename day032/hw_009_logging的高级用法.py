# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 07:06
# 文件名称: hw_009_logging的高级用法.py
# 开发工具: PyCharm

"""
logging配置
"""

import os
import logging.config

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'  # 其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
zhangdapeng = '[%(levelname)s]%(lineno)d行:%(message)s'
logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
# print('--' * 22)
# print(logfile_dir)
# print("%s/log" % logfile_dir)
# 当前文件夹下的log文件夹
logfile_dir = "%s/log" % logfile_dir
logfile_name = 'log.log'  # log文件名
# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)
# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)
# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'id_simple_format': {
            'format': id_simple_format
        },
        'zhangdapeng': {
            'format': zhangdapeng
        }

    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            # 'formatter': 'simple'
            # 'formatter': 'id_simple_format'
            'formatter': 'zhangdapeng'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}

logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
logger = logging.getLogger(__name__)  # 生成一个log实例
logger.info("测试")
