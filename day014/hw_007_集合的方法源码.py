# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 07:57
# 文件名称: hw_007_集合的方法源码.py
# 开发工具: PyCharm
class set(object):
    """
    set() -> new empty set object
    创建空集合
    set(iterable) -> new set object
    根据可迭代对象创建新的集合对象
    Build an unordered collection of unique elements.
    创建一个无序的元素唯一的集合
    """

    def add(self, *args, **kwargs):  # real signature unknown
        """
        Add an element to a set.
        向集合中添加一个新的元素
        This has no effect if the element is already present.
        如果集合中已存在该元素则不产生影响
        """
        pass

    def clear(self, *args, **kwargs):  # real signature unknown
        """
        Remove all elements from this set.
        清空集合中所有的元素
        """
        pass

    def copy(self, *args, **kwargs):  # real signature unknown
        """
        Return a shallow copy of a set.
        返回集合的浅拷贝
        """
        pass

    def difference(self, *args, **kwargs):  # real signature unknown
        """
        Return the difference of two or more sets as a new set.
        返回两个或更多的新集合
        (i.e. all elements that are in this set but not the others.)
        """
        pass

    def difference_update(self, *args, **kwargs):  # real signature unknown
        """
        Remove all elements of another set from this set.
        根据这个集合删除另一个集合中的所有包含此集合元素的内容
        """
        pass

    def discard(self, *args, **kwargs):  # real signature unknown
        """
        Remove an element from a set if it is a member.
        如果此集合是成员,删除
        If the element is not a member, do nothing.
        不是则不产生影响
        """
        pass

    def intersection(self, *args, **kwargs):  # real signature unknown
        """
        Return the intersection of two sets as a new set.
        将两个集合合并为新的集合 交集
        (i.e. all elements that are in both sets.)
        """
        pass

    def intersection_update(self, *args, **kwargs):  # real signature unknown
        """
        Update a set with the intersection of itself and another.
        """
        pass

    def isdisjoint(self, *args, **kwargs):  # real signature unknown
        """
        Return True if two sets have a null intersection.
        """
        pass

    def issubset(self, *args, **kwargs):  # real signature unknown
        """
        Report whether another set contains this set.
        """
        pass

    def issuperset(self, *args, **kwargs):  # real signature unknown
        """ Report whether this set contains another set. """
        pass

    def pop(self, *args, **kwargs):  # real signature unknown
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        pass

    def remove(self, *args, **kwargs):  # real signature unknown
        """
        Remove an element from a set; it must be a member.

        If the element is not a member, raise a KeyError.
        """
        pass

    def symmetric_difference(self, *args, **kwargs):  # real signature unknown
        """
        Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)
        """
        pass

    def symmetric_difference_update(self, *args, **kwargs):  # real signature unknown
        """ Update a set with the symmetric difference of itself and another. """
        pass

    def union(self, *args, **kwargs):  # real signature unknown
        """
        Return the union of sets as a new set.

        (i.e. all elements that are in either set.)
        """
        pass

    def update(self, *args, **kwargs):  # real signature unknown
        """ Update a set with the union of itself and others. """
        pass

