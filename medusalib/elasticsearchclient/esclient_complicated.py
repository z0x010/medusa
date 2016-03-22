#!/usr/bin/env python
# coding:utf-8

"""
放弃使用模块方式实现的ElasticSearch单例
(仅供参考，不在web服务中使用)
"""


from pyelasticsearch import ElasticSearch


class Singleton(object):
    """
    单例模式
    """
    def __new__(cls, *args, **kwargs):
        print cls.__name__, '__new__', '(Singleton)'
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            print cls.__name__, '__new__', '(created a new instance: %s: %s)' % (cls.__name__, id(cls._instance))
        return cls._instance


class ESClient(Singleton):
    """
    Elasticsearch Client (单例模式)
    """
    def __new__(cls, *args, **kwargs):
        print cls.__name__, '__new__', '(ESClient)'
        cls._instance = super(ESClient, cls).__new__(cls, *args, **kwargs)
        """
        要实现 esclient 连接对象的单例模式，
        必须把创建 esclient 连接对象操作写在 __new__ 中！
        """
        if not hasattr(cls._instance, 'esclient'):
            cls.esclient = ElasticSearch(
                urls='http://192.168.100.100',
                port=9200,
            )
            print cls.__name__, '__new__', '(created a new instance: %s: %s)' % (cls.esclient.__class__.__name__, id(cls.esclient))
        return cls._instance

    def __init__(self):
        print self.__class__.__name__, '__init__'
        """
        创建连接的操作放在 __init__ 中就不是单例模式了，
        每次创建得到的虽然是同一个 ESClient 实例，但是每次都会重新创建 esclient 连接对象！
        想要实现连接的单例模式，需要把创建 esclient 连接对象的操作写在 __new__ 中！
        """
        # self.esclient = ElasticSearch(
        #     urls='http://192.168.100.100',
        #     port=9200,
        # )
        pass


if __name__ == '__main__':
    print '================================================== 1111111111'
    a = ESClient()
    print id(a)
    print id(a.esclient)
    print '================================================== 2222222222'
    b = ESClient()
    print id(b)
    print id(b.esclient)
    # ================================================== 1111111111
    # ESClient __new__ (ESClient)
    # ESClient __new__ (Singleton)
    # ESClient __new__ (created a new instance: ESClient: 4366643472)        # !!!!!!!!!! 创建单例
    # ESClient __new__ (created a new instance: ElasticSearch: 4372157968)   # !!!!!!!!!! 创建单例
    # ESClient __init__
    # 4366643472
    # 4372157968
    # ================================================== 2222222222
    # ESClient __new__ (ESClient)
    # ESClient __new__ (Singleton)
    # ESClient __init__
    # 4366643472
    # 4372157968
