#!/usr/bin/env python
# coding:utf-8

import re

print '=============================================================================='
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d*')
# <_sre.SRE_Pattern object at 0x106994b70>

# 使用Pattern[匹配]文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('123ABC456ABCDEFG789')
# <_sre.SRE_Match object at 0x10d065850>

print match
if match:
    # 使用Match获得分组信息
    print match.group()
    # <type 'str'>
print '=============================================================================='
# 将正则表达式编译成Pattern对象
pattern = re.compile(r'\d*')
# <_sre.SRE_Pattern object at 0x106994b70>

# 使用Pattern[搜索]文本，获得搜索结果，不存在能匹配的子串时将返回None
match = pattern.search('123ABC456ABCDEFG789')
# <_sre.SRE_Match object at 0x10a4eb850>

print match
if match:
    # 使用Match获得分组信息
    print match.group()
print '=============================================================================='
print pattern.split('123ABC456ABCDEFG789')
# ['', 'ABC', 'ABCDEFG', '']
print '=============================================================================='
