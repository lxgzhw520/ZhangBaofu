# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 06:25
# 文件名称: hw_003_对象复习.py
# 开发工具: PyCharm
import logging

logger = logging.getLogger(name="张大鹏")
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class Person:
    id_count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        # 实现id自增
        Person.id_count += 1
        self.__id = Person.id_count

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def show(self):
        logging.info("ID:{}\n姓名:{}\n年龄:{}\n".format(
            self.__id, self.__name, self.__age
        ))


class Student(Person):
    @classmethod
    def who(cls):
        logging.info("我是学生")

    @staticmethod
    def add():
        logging.info("我可以计算加法")


zbf = Student('张宝富', 33)
zbf.show()
zbf.who()
zbf.add()
