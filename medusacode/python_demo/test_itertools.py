#!/usr/bin/env python
# coding:utf-8
"""
itertools — Functions creating iterators for efficient looping
"""

import itertools


"""
Infinite Iterators
"""
print '--------------------------------------------------------------------------------------------------'
# [1] count
count = itertools.count(1, 2)  # Infinite Iterators
# 1 3 5 7 9 ...

# [2] cycle
cycle = itertools.cycle('123')  # <type 'itertools.cycle'>
# 1 2 3 1 2 3 1 2 3 ...

# [3] repeat
repeat = itertools.repeat(1)  # <type 'itertools.repeat'>
# 1 1 1 1 1 ...
print '--------------------------------------------------------------------------------------------------'


"""
Iterators terminating on the shortest input sequence
"""
print '--------------------------------------------------------------------------------------------------'
chain = itertools.chain([1, 2, 3], [4, 5, 6])
# 1 2 3 4 5 6

compress = itertools.compress([1, 2, 3, 4, 5], [1, 0, 1, 0, 1])
# 1 3 5

dropwhile = itertools.dropwhile(lambda x: x < 3, [1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
# 3 4 5 1 2 3 4 5

takewhile = itertools.takewhile(lambda x: x < 3, [1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
# 1 2

groupby = itertools.groupby([1, 2, 2, 3, 3, 3], key=lambda x: x+10)
# (11, <itertools._grouper object at 0x1029d4250>)  # 1
# (12, <itertools._grouper object at 0x1029d4290>)  # 2 2
# (13, <itertools._grouper object at 0x1029d4250>)  # 3 3 3

ifilter = itertools.ifilter(lambda x: x % 2, [1, 2, 3, 4, 5])
# 1 3 5

ifilterfalse = itertools.ifilterfalse(lambda x: x % 2, [1, 2, 3, 4, 5])
# 2 4

islice = itertools.islice([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 8, 2)
# 3 5 7

imap = itertools.imap(pow, [1, 2, 3], [1, 2, 3])
# 1 4 27

starmap = itertools.starmap(pow, [[1, 1], [2, 2], [3, 3]])
# 1 4 27

tee = itertools.tee([1, 2, 3], 3)
# 1 2 3
# 1 2 3
# 1 2 3

izip = itertools.izip(['a', 'b', 'c'], [1, 2, 3, 4])
# ('a', 1) ('b', 2) ('c', 3)

izip_longest = itertools.izip_longest(['a', 'b', 'c'], [1, 2, 3, 4], fillvalue='X')
# ('a', 1) ('b', 2) ('c', 3) ('X', 4)
print '--------------------------------------------------------------------------------------------------'


"""
Combinatoric generators
"""
print '--------------------------------------------------------------------------------------------------'
product = itertools.product('1234', repeat=3)
# 笛卡尔积
# ('1', '1', '1')
# ('1', '1', '2')
# ('1', '1', '3')
# ('1', '1', '4')
# ... 4**3=64

permutations = itertools.permutations('123', 2)
# 排列
# ('1', '2')
# ('1', '3')
# ('2', '1')
# ('2', '3')
# ('3', '1')
# ('3', '2')

combinations = itertools.combinations('123', 2)
# 组合
# ('1', '2')
# ('1', '3')
# ('2', '3')

combinations_with_replacement = itertools.combinations_with_replacement('123', 2)
# 组合（包含元素重复）
# ('1', '1')
# ('1', '2')
# ('1', '3')
# ('2', '2')
# ('2', '3')
# ('3', '3')
print '--------------------------------------------------------------------------------------------------'
