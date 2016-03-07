#!/usr/bin/env python
# coding=utf-8

"""
分析词频:李克强政府工作报告
"""

import jieba
import time
from collections import Counter

text = open('text.txt').read()

generator_jieba = jieba.cut(text)  # <generator object cut at 0x107ab2b40>
print type(generator_jieba)  # <type 'generator'>

counter = Counter(generator_jieba)  # Counter({ ... })
print type(counter)  # <class 'collections.Counter'>

exclude = [u'\n', u'的', u'，', u'。', u'、', u'%', u'"']
for e in exclude:
    counter.pop(e)

time.sleep(1)
for word, count in counter.most_common(20):
    print '[%s]' % word, count
