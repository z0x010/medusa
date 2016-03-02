#!/usr/bin/env python
# coding:utf-8

"""
请求 ElasticSearch web service 获取搜索结果
"""

import json
import requests


def es_search(es_dsl):
    response = requests.get(url='http://192.168.100.100:8000/es/search/', params={'dsl': json.dumps(es_dsl)})
    # ret = response.json()  # <type 'dict'>
    # ret = response.text  # <type 'unicode'>
    # ret = response.content  # <type 'str'>
    return response.content


# ---------------------------------------------------------------------------------------- [Filter]
# term Filter
dsl = {
    'filter': {
        'term': {
            'rank': 1,
        }
    }
}

# terms Filter
dsl = {
    'filter': {
        'terms': {
            'rank': [1, 2, 3],
        }
    }
}

# range Filter
dsl = {
    'filter': {
        'range': {
            'rank': {
                'gt': 1,
                'lt': 4,
            }
        }
    }
}

# exists Filters
dsl = {
    'filter': {
        'exists': {
            'field': 'rank'
        }
    }
}

# missing Filters
dsl = {
    'filter': {
        'missing': {
            'field': 'rank'
        }
    }
}

# bool Filter
"""
The bool filter is used to combine multiple filter clauses using Boolean logic.
It accepts three parameters:
must: These clauses must match, like and.
must_not: These clauses must not match, like not.
should: At least one of these clauses must match, like or.
"""
dsl = {
    'filter': {
        'bool': {
            # must 必须符合
            'must': {
                'terms': {
                    'rank': [1, 2, 3, 4],
                }
            },
            # must_not 必须不符
            'must_not': {
                'terms': {
                    'rank': [1, 4]
                }
            },
            # should 必须至少符合其一
            'should': [
                {
                    'term': {
                        'rank': 1
                    }
                },
                {
                    'term': {
                        'rank': 2
                    }
                }
            ],
        }
    }
}
# ---------------------------------------------------------------------------------------- [Filter]
# ---------------------------------------------------------------------------------------- [Query]
# match_all Query
dsl = {
    'query': {
        'match_all': {
        }
    }
}

# match Query
dsl = {
    'query': {
        'match': {
            'rank': 1
        }
    }
}
dsl = {
    'query': {
        'match': {
            'desc': 'Spacey'
        }
    }
}

# multi_match Query
"""
The multi_match query allows to run the same match query on multiple fields.
"""
dsl = {
    'query': {
        'multi_match': {
            'query': 'David',
            'fields': ['title', 'quote', 'desc'],
        }
    }
}

# bool Query
"""
The bool query, like the bool filter, is used to combine multiple query clauses. However, there are some differences.
    filters give binary yes/no answers,
    queries calculate a relevance score instead.
The bool query combines the _score from each must or should clause that matches.This query accepts the following parameters:
    must: Clauses that must match for the document to be included.
    must_not: Clauses that must not match for the document to be included.
    should: If these clauses match, they increase the _score; otherwise, they have no effect.
            They are simply used to refine the relevance score for each document.
If there are no must clauses, at least one should clause has to match.
If there is at least one must clause, no should clauses are required to match.
"""
dsl = {
    'query': {
        'bool': {
            # must 必须符合
            'must': {
                'match': {
                    'desc': 'Spacey'
                }
            },
            # must_not 必须不符
            'must_not': {
                'match': {
                    'desc': 'Sam'
                }
            },
            # should 如果满足会增加相关性得分
            'should': [
                {
                    'match': {
                        'desc': 'Curtis'
                    }
                },
                {
                    'match': {
                        'desc': 'Hanson'
                    }
                }
            ],
        }
    }
}
# ---------------------------------------------------------------------------------------- [Query]
ret = es_search(dsl)
print ret

