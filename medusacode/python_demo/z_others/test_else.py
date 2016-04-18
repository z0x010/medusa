#!/usr/bin/env python
# coding=utf-8

"""
循环中的 else
"""

"""
循环中的 else
    [1] 跟在循环后面的 else 语句只有在循环内没出现 break，也就是正常循环完成时才会执行。
"""
for n in range(5, 0, -1):
    try:
        print n, 100/n
    except Exception, e:
        print e
        break
else:
    print '[else] (no break)'

"""
循环中的 else
    [2] 没有循环的时候也会触发后面的 else 语句。
"""
l = []
for n in l:
    print n
else:
    print '[else] (no loop)'


"""
错误捕捉中的 else
    try...except...else...finally 流程控制语法用于捕捉可能出现的异常并进行相应的处理
        except 用于捕捉 try 语句中出现的错误;
        else 则用于处理没有出现错误的情况;
        finally 负责 try 语句的”善后工作“ ，无论如何都会执行。
"""

try:
    print 'try'
    print 1/0
except:
    print 'except'
else:
    print 'else'
finally:
    print 'finally'
# try
# except
# finally

try:
    print 'try'
    print 1/1
except:
    print 'except'
else:
    print 'else'
finally:
    print 'finally'
# try
# else
# finally
