# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 07:44
# 文件名称: hw_005_字典的方法源码.py
# 开发工具: PyCharm
class dict(object):
    """
    dict() -> new empty dictionary
    dict() -> 生成一个空的字典
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    根据给定的mapping对应关系初始化为一个新的字典
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    如果是可迭代对象,会遍历迭代对象生成一个新的字典
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    根据键值对生成一个新的字典
    """

    def clear(self):  # real signature unknown; restored from __doc__
        """
        D.clear() -> None.  Remove all items from D.
        移除字典中的所有元素
        """
        pass

    def copy(self):  # real signature unknown; restored from __doc__
        """
        D.copy() -> a shallow copy of D
        对字典进行浅拷贝
        """
        pass

    @staticmethod  # known case
    def fromkeys(*args, **kwargs):  # real signature unknown
        """
        Create a new dictionary with keys from iterable and values set to value.
        从可迭代对象和值集合中根据键创建一个新的字典
         """
        pass

    def get(self, *args, **kwargs):  # real signature unknown
        """
        Return the value for key if key is in the dictionary, else default.
        如果键在字典中,返回键对应的值,否则返回默认值
        """
        pass

    def items(self):  # real signature unknown; restored from __doc__
        """
        D.items() -> a set-like object providing a view on D's items
        返回字典的元素
        """
        pass

    def keys(self):  # real signature unknown; restored from __doc__
        """
        D.keys() -> a set-like object providing a view on D's keys
        返回字典的键
        """
        pass

    def pop(self, k, d=None):  # real signature unknown; restored from __doc__
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        移除指定的键并返回
        如果不存在,会抛出异常
        """
        pass

    def popitem(self):  # real signature unknown; restored from __doc__
        """
        D.popitem() -> (k, v), remove and return some (key, value) pair as a
        2-tuple; but raise KeyError if D is empty.
        移除指定的键值对并返回一个键值对元素
        不存在会报错
        """
        pass

    def setdefault(self, *args, **kwargs):  # real signature unknown
        """
        Insert key with a value of default if key is not in the dictionary.
        如果键不在字典中,插入一个带有默认值的键
        Return the value for key if key is in the dictionary, else default.
        如果键在字典中,返回该键对应的值
        """
        pass

    def update(self, E=None, **F):  # known special case of dict.update
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        根据字典或可迭代对象更新字典
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        pass

    def values(self):  # real signature unknown; restored from __doc__
        """
        D.values() -> an object providing a view on D's values
        返回字典中的键对应的值
        """
        pass
