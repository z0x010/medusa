#!/usr/bin/env python
# coding:utf-8

import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'1[0-9]{0,100}$')
# <_sre.SRE_Pattern object at 0x106994b70>

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
# match = pattern.match('123456789')
match = re.match(pattern, '123456789')
# <_sre.SRE_Match object at 0x10d065850>

if match:
    # 使用Match获得分组信息
    print match.group()
    # <type 'str'>
