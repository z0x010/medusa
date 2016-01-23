#!/usr/bin/env python
# coding:utf-8


def bread(func):
    def wrapper():
        print "</''''''\>"
        func()
        print "<\______/>"
    return wrapper

def ingredients(func):
    def wrapper():
        print "#tomatoes#"
        func()
        print "~salad~"
    return wrapper

def sandwich(food="--ham--"):
    print food


sandwich_1 = bread(ingredients(sandwich))
sandwich_1()
# outputs:
# </''''''\>
# #tomatoes#
# --ham--
# ~salad~
# <\______/>


@bread
@ingredients
def sandwich_2(food="--ham--"):
    print food

sandwich_2()
# outputs:
# </''''''\>
# #tomatoes#
# --ham--
# ~salad~
# <\______/>

