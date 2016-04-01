#!/usr/bin/env python
# coding:utf-8

"""
请求 ElasticSearch client 获取搜索结果
"""

from es_0_lib import search_dsl

# ----------------------------------------------------------------------------------------------------

# 精确匹配
dsl_term = {
    'query': {
        'term': {
            'rank': 1,
        }
    }
}

# 精确匹配
dsl_terms = {
    'query': {
        'terms': {
            'rank': [1, 2, 3],
        }
    }
}

# 范围匹配
dsl_range = {
    'query': {
        'range': {
            'rank': {
                'gte': 1,
                'lte': 3,
            }
        }
    }
}

# 布尔过滤
# must=and, must_not=not, should=or
dsl_bool = {
    'query': {
        'bool': {
            'must': {
                'terms': {
                    'rank': [1, 2, 3],
                }
            },
            'must_not': {
                'terms': {
                    'rank': [3, 4, 5],
                }
            },
            'should': [
                {
                    'term': {
                        'rank': 1,
                    }
                },
                {
                    'term': {
                        'rank': 2,
                    }
                },
                {
                    'term': {
                        'rank': 3,
                    }
                }
            ]
        }
    }
}

# 布尔过滤
# must=and, must_not=not, should=or
dsl_must = {
    'query': {
        'bool': {
            'must': [
                {
                    'match': {
                        'desc': 'Spacey',
                    }
                },
                {
                    'match': {
                        'title': 'Moon',
                    }
                },
                {
                    'match': {
                        'rate': 8.5,
                    }
                }
            ]
        }
    }
}

# 布尔过滤
# must=and, must_not=not, should=or
dsl_should = {
    'query': {
        'bool': {
            'should': [
                {
                    'match': {
                        'desc': 'Spacey',
                    }
                },
                {
                    'match': {
                        'title': 'Moon',
                    }
                },
                {
                    'match': {
                        'rate': 8.5,
                    }
                }
            ]
        }
    }
}

# 匹配查询
dsl_match = {
    'query': {
        'match': {
            'rank': 1,
        }
    }
}
# ----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    search_dsl(dsl_should)
    pass
