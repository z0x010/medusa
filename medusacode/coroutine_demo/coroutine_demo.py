#!/usr/bin/env python
# coding=utf-8

"""
The yield expression is only used when defining a generator function,
and can only be used in the body of a function definition.
Using a yield expression in a function definition is sufficient to
cause that definition to create a generator function instead of a normal function.

When a generator function is called, it returns an iterator known as a generator.
That generator then controls the execution of a generator function.
The execution starts when one of the generator’s methods is called.
At that time, the execution proceeds to the first yield expression,
where it is suspended again, returning the value of expression_list to generator’s caller.
By suspended we mean that all local state is retained,
including the current bindings of local variables, the instruction pointer, and the internal evaluation stack.
When the execution is resumed by calling one of the generator’s methods,
the function can proceed exactly as if the yield expression was just another external call.
The value of the yield expression after resuming depends on the method which resumed the execution.

All of this makes [generator functions] quite similar to [coroutines];
they yield multiple times, they have more than one entry point and their execution can be suspended.
The only difference is that a generator function cannot control where should the execution continue after it yields;
the control is always transferred to the generator’s caller.
"""

"""
传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
如果改用协程(coroutine)，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高。
"""

import time

def produce():
    n = 0
    while n <= 5:
        print '[producer] producing %s ...' % n
        time.sleep(0.5)
        yield n
        n += 1

def consume(producer):
    print '------------------------------ start consume'
    while True:
        try:
            item = producer.next()
            print '[consumer] get item from [producer]: %s' % item
            print '[consumer] consuming %s' % item
        except StopIteration, e:
            print type(e), e
            break
    print '------------------------------ stop consume'
    producer.close()

if __name__ == '__main__':
    print type(produce), produce  # <type 'function'> <function produce at 0x106c0e668>
    p = produce()
    print type(p), p  # <type 'generator'> <generator object produce at 0x106cd1230>
    consume(p)
