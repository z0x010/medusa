#!/usr/bin/env python
# coding:utf-8


import json

print '============================================================================ ElasticSearch'
from pyelasticsearch import ElasticSearch
es = ElasticSearch(
    urls='http://192.168.100.100',
    port=9200,
)
print '============================================================================ DSL'
"""
DSL(Domain Specific Language)
"""
# ----------------------------------------------------------------------------------------------------

# 精确匹配
# dsl_term = {
#     'query': {
#         'term': {
#             'rank': 1,
#         }
#     }
# }

# 精确匹配
# dsl_terms = {
#     'query': {
#         'terms': {
#             'rank': [1, 2, 3],
#         }
#     }
# }

# 范围匹配
# dsl_range = {
#     'query': {
#         'range': {
#             'rank': {
#                 'gte': 1,
#                 'lte': 3,
#             }
#         }
#     }
# }

# 布尔过滤
# must=and, must_not=not, should=or
# dsl_bool = {
#     'query': {
#         'bool': {
#             'must': {
#                 'terms': {
#                     'rank': [1, 2, 3],
#                 }
#             },
#             'must_not': {
#                 'terms': {
#                     'rank': [3, 4, 5],
#                 }
#             },
#             'should': [
#                 {
#                     'term': {
#                         'rank': 1,
#                     }
#                 },
#                 {
#                     'term': {
#                         'rank': 2,
#                     }
#                 },
#                 {
#                     'term': {
#                         'rank': 3,
#                     }
#                 }
#             ]
#         }
#     }
# }

# 匹配查询
# dsl_match = {
#     'query': {
#         'match': {
#             'rank': 1,
#         }
#     }
# }

# ----------------------------------------------------------------------------------------------------
# dsl_movie = {
#     'query': {
#         'bool': {
#             'must': [
#                 {
#                     'match': {
#                         'desc': '美国',
#                     }
#                 },
#                 {
#                     'match': {
#                         'quote': '美国',
#                     }
#                 },
#                 {
#                     'match': {
#                         'star': 5.0,
#                     }
#                 }
#             ]
#         }
#     }
# }
# ----------------------------------------------------------------------------------------------------
# keyword = '美国'
# dsl_movie = {
#     'query': {
#         'bool': {
#             'should': [
#                 {
#                     'match': {
#                         'title': keyword,
#                     }
#                 },
#                 {
#                     'match': {
#                         'desc': keyword,
#                     }
#                 },
#                 {
#                     'match': {
#                         'quote': keyword,
#                     }
#                 }
#             ]
#         }
#     }
# }
# ----------------------------------------------------------------------------------------------------
print '============================================================================ DSL'
"""
Match All Query
"""
dsl_match_all = {
    'query': {
        'match_all': {}
    }
}

"""
Match Query
"""
dsl_match = {
    'query': {
        'match': {
            'rank': 1
        }
    }
}

"""
Multi Match Query
"""
dsl_multi_match = {
    'query': {
        'multi_match': {
            'query': 'Shawshank',
            'fields': ['title', 'quote', 'desc'],
        }
    }
}

# ----------------------------------------------------------------------------------------------------
search = es.search(
    index='douban',
    doc_type='movie',
    query=dsl_multi_match,
)
print json.JSONEncoder(indent=4).encode(search)
