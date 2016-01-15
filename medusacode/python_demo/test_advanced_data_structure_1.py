#!/usr/bin/env python
# coding:utf-8
"""
Python 非常用的高级数据结构
"""


print '--------------------------------------------------------------------------------------------------'
# enumerate
l = ['A', 'B', 'C', 'D', 'E']
e = enumerate(l)
e = enumerate(l, start=1)
print type(e), e
for t in e:
    print type(t), t
    pass
# <type 'enumerate'> <enumerate object at 0x1002f0e60>
# <type 'tuple'> (1, 'A')
# <type 'tuple'> (2, 'B')
# <type 'tuple'> (3, 'C')
# <type 'tuple'> (4, 'D')
# <type 'tuple'> (5, 'E')
print '--------------------------------------------------------------------------------------------------'
# set
l1 = ['A', 'B', 'C', 'D', 'E']
l2 = ['C', 'D', 'E', 'F', 'G']
s1 = set(l1)
s2 = set(l2)
# 交集
print s1.intersection(s2)
# 并集
print s1.union(s2)
# 差集
print s1.difference(s2)
# 对称差集
print s1.symmetric_difference(s2)
# set(['C', 'E', 'D'])
# set(['A', 'C', 'B', 'E', 'D', 'G', 'F'])
# set(['A', 'B'])
# set(['A', 'B', 'G', 'F'])
print '--------------------------------------------------------------------------------------------------'
# collections.namedtuple
# factory function for creating tuple subclasses with named fields
import collections
lightObject = collections.namedtuple('typename_lightObject', ['name', 'age'])
person = lightObject(name='omoplata', age=30)
print person.name
print person.age
# omoplata
# 30
print '--------------------------------------------------------------------------------------------------'
# collections.defaultdict
# dict subclass that calls a factory function to supply missing values
# 使用defaultdict可以跳过检查关键字是否存在的逻辑，对某个未定义key的任意访问，都会返回一个空列表（或者其他数据类型）
import collections
dd = collections.defaultdict(list)
print type(dd), dd
print dd['key1']
print dd
print dd['key2']
print dd
dd['key1'].append('value1')
print dd
# <type 'collections.defaultdict'> defaultdict(<type 'list'>, {})
# []
# defaultdict(<type 'list'>, {'key1': []})
# []
# defaultdict(<type 'list'>, {'key2': [], 'key1': []})
# defaultdict(<type 'list'>, {'key2': [], 'key1': ['value1']})
print '--------------------------------------------------------------------------------------------------'
# collections.Counter
# dict subclass for counting hashable objects
import collections
l = ['A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D', 'D']
c = collections.Counter(l)
print type(c), c
print c['A']
print c['Z']
print c.elements()
for e in c.elements():
    print e
    pass
print c.most_common(3)
# <class 'collections.Counter'> Counter({'D': 4, 'C': 3, 'B': 2, 'A': 1})
# 1
# 0
# <itertools.chain object at 0x1002817d0>
# [('D', 4), ('C', 3), ('B', 2)]
print '--------------------------------------------------------------------------------------------------'
# collections.deque
# (the name is pronounced “deck” and is short for “double-ended queue”)
# list-like container with fast appends and pops on either end
import collections
l = ['A', 'B', 'C', 'D', 'E']
dq = collections.deque(l)
print type(dq), dq
dq.appendleft('LEFT')
print dq
dq.extendleft(['LA', 'LB', 'LC'])
print dq
dq.rotate(5)
print dq
dq.reverse()
print dq
# <type 'collections.deque'> deque(['A', 'B', 'C', 'D', 'E'])
# deque(['LEFT', 'A', 'B', 'C', 'D', 'E'])
# deque(['LC', 'LB', 'LA', 'LEFT', 'A', 'B', 'C', 'D', 'E'])
# deque(['A', 'B', 'C', 'D', 'E', 'LC', 'LB', 'LA', 'LEFT'])
# deque(['LEFT', 'LA', 'LB', 'LC', 'E', 'D', 'C', 'B', 'A'])
print '--------------------------------------------------------------------------------------------------'
# collections.OrderedDict
# dict subclass that remembers the order entries were added
import collections
d = {}
od = collections.OrderedDict()
for k, v in (('a', 1), ('b', 2), ('c', 3)):
    d[k] = v
    od[k] = v
    pass
print type(d)
print d
print type(od)
print od
# <type 'dict'>
# {'a': 1, 'c': 3, 'b': 2}
# <class 'collections.OrderedDict'>
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print '--------------------------------------------------------------------------------------------------'
