#!/usr/bin/env python
# coding:utf-8

from pyelasticsearch import ElasticSearch

"""
class pyelasticsearch.ElasticSearch(
    urls='http://localhost',
    timeout=60,
    max_retries=0,
    port=9200,
    username=None,
    password=None,
    ca_certs='cacert.pem',
    client_cert=None)

    An object which manages connections to elasticsearch and acts as a go-between for API calls to it.
    This object is thread-safe. You can create one instance and share it among all threads.
"""

es_client = ElasticSearch(
    urls='http://192.168.100.100',
    port=9200,
)

"""
Python的模块(module)，就是最 pythonic 的 singleton 典范。
模块在在一个应用程序中只有一份，它本身就是单例的。
所以只要将所需要的属性和方法，直接暴露在模块中变成模块的全局变量和全局方法即可！
"""
