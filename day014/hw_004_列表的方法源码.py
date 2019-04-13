# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 07:36
# 文件名称: hw_004_列表的方法源码.py
# 开发工具: PyCharm
class list(object):
    """
    Built-in mutable sequence.

    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified.
    如果不给参数,就返回空列表
    参数必须是可迭代的数据类型
    """

    def append(self, *args, **kwargs):  # real signature unknown
        """
        Append object to the end of the list.
        在列表的末尾追加一个新的元素
        """
        pass

    def clear(self, *args, **kwargs):  # real signature unknown
        """
        Remove all items from list.
        移除列表中所有的元素
        """
        pass

    def copy(self, *args, **kwargs):  # real signature unknown
        """
        Return a shallow copy of the list.
        返回列表的浅拷贝
        """
        pass

    def count(self, *args, **kwargs):
        """
        Return number of occurrences of value.
        返回给定的值的数量
        """
        pass

    def extend(self, *args, **kwargs):  # real signature unknown
        """
        Extend list by appending elements from the iterable.
        从可迭代对象中扩展一个新的列表追加到元素末尾
         """
        pass

    def index(self, *args, **kwargs):  # real signature unknown
        """
        Return first index of value.
        返回给定值的第一个索引
        Raises ValueError if the value is not present.
        如果不存在就抛出错误
        """
        pass

    def insert(self, *args, **kwargs):  # real signature unknown
        """
        Insert object before index.
        在给定索引位置的前面插入一个对象
        """
        pass

    def pop(self, *args, **kwargs):  # real signature unknown
        """
        Remove and return item at index (default last).
        移除指定索引位置的元素,默认是最后一个
        Raises IndexError if list is empty or index is out of range.
        如果列表为空或者索引超出范围会抛出索引错误
        """
        pass

    def remove(self, *args, **kwargs):  # real signature unknown
        """
        Remove first occurrence of value.
        移除找到的第一个值

        Raises ValueError if the value is not present.
        如果值不存在就抛出值错误
        """
        pass

    def reverse(self, *args, **kwargs):  # real signature unknown
        """
        Reverse *IN PLACE*.
        反转  内部代替 意思是说值被真的改变了,而不是生成拷贝内容
        """
        pass
