#!/usr/bin/env python
# coding:utf-8

import re

print '------------------------------------------------------------------------------'
"""
Python offers two different primitive operations based on regular expressions:
    re.match() checks for a match only at the beginning of the string,
    re.search() checks for a match anywhere in the string (this is what Perl does by default).
"""
print '------------------------------------------------------------------------------'
"""
re.match(pattern, string, flags=0)
    If zero or more characters at the beginning of string match the regular expression pattern,
    return a corresponding MatchObject instance. Return None if the string does not match the pattern;
    If you want to locate a match anywhere in string, use search() instead.
"""
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d*')
# <_sre.SRE_Pattern object at 0x106994b70>

# 使用Pattern[匹配]文本，获得匹配结果，无法匹配时将返回None
# match = pattern.match('123ABC456ABCDEFG789')
match = re.match(pattern, '123ABC456ABCDEFG789')
# <_sre.SRE_Match object at 0x10d065850>

print match
if match:
    # 使用Match获得分组信息
    print match.group()
    # <type 'str'>
    print match.start(), match.end()
    # 0 3
print '------------------------------------------------------------------------------'
"""
re.search(pattern, string, flags=0)
    Scan through string looking for the first location where the regular expression pattern produces a match,
    and return a corresponding MatchObject instance. Return None if no position in the string matches the pattern.
"""
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d*')
# <_sre.SRE_Pattern object at 0x106994b70>

# 使用Pattern[搜索]文本，获得搜索结果，不存在能匹配的子串时将返回None
# match = pattern.search('123ABC456ABCDEFG789')
match = re.search(pattern, '123ABC456ABCDEFG789')
# <_sre.SRE_Match object at 0x10a4eb850>

print match
if match:
    # 使用Match获得分组信息
    print match.group()
    # <type 'str'>
    print match.start(), match.end()
    # 0 3
print '------------------------------------------------------------------------------'
"""
re.findall(pattern, string, flags=0)
    Return all non-overlapping matches of pattern in string, as a list of strings.
    The string is scanned left-to-right, and matches are returned in the order found.
    If one or more groups are present in the pattern, return a list of groups;
    this will be a list of tuples if the pattern has more than one group.
    Empty matches are included in the result unless they touch the beginning of another match.
"""
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d*')
# <_sre.SRE_Pattern object at 0x106994b70>

findall = re.findall(pattern, '123ABC456ABCDEFG789')
# <type 'list'>
print findall
# ['123', '', '', '', '456', '', '', '', '', '', '', '', '789', '']
print '------------------------------------------------------------------------------'
"""
re.split()
"""
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d*')
# <_sre.SRE_Pattern object at 0x106994b70>

# print pattern.split('123ABC456ABCDEFG789')
print re.split(pattern, '123ABC456ABCDEFG789')
# ['', 'ABC', 'ABCDEFG', '']
print '------------------------------------------------------------------------------'
