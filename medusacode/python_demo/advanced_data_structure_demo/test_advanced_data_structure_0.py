#!/usr/bin/env python
# coding:utf-8

# ---------------------------------------------------------------------------------------------- [OK]
# [OrderedDict][dict subclass that remembers the order entries were added]

from collections import OrderedDict
d1 = {}
d1['a'] = 1
d1['b'] = 2
d1['c'] = 3
print d1
# {'a': 1, 'c': 3, 'b': 2}
d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2
d2['c'] = 3
print d2
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# ---------------------------------------------------------------------------------------------- [OK]
# [Counter][dict subclass for counting hashable objects]

from collections import Counter
l = [1, 2, 3, 'A', 'B', 'C', 1, 2, 3, 4, 5, 6, (1, 2, 3)]
print l
print sorted(l)
print Counter(l)
# ---------------------------------------------------------------------------------------------- [OK]
# [deque][list-like container with fast appends and pops on either end]

from collections import deque
deq = deque(range(5))
print deq
deq.pop()
print deq
deq.popleft()
print deq
deq.append(9)
print deq
deq.appendleft(-1)
print deq
deq.rotate(1)
print deq
deq.rotate(-2)
print deq
# ---------------------------------------------------------------------------------------------- [OK]
# [defaultdict][dict subclass that calls a factory function to supply missing values]

from collections import defaultdict
s = 'Once opon a time , there was a superhero called batman , and another superhero named superman .'
words = s.split()
print words
location = defaultdict(list)
print location
for w in enumerate(words):
    print w
    location[w[1]].append(w[0])
print location
# ---------------------------------------------------------------------------------------------- [OK]
