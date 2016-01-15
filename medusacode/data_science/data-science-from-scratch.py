#!/usr/bin/env python
# coding:utf-8

from __future__ import division  # 引入整数除法特性
from collections import Counter
from collections import defaultdict

print '-----------------------------------------------------------------------------'
# 用户
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]
# 友谊关系
friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]
for user in users:
    user["friends"] = []
    pass
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])
    pass
print '-----------------------------------------------------------------------------'
# 朋友关系统计
print 'id, name, friend_id'
for user in users:
    print user['id'], user['name'], [f['id'] for f in user['friends']]
    pass
# 朋友数量
def number_of_friends(user):
    return len(user["friends"])
# 朋友关系数量
total_connections = sum(number_of_friends(user) for user in users)
# print total_connections
print '-----------------------------------------------------------------------------'
# 朋友数量统计
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print num_friends_by_id
# 朋友数量排序
print sorted(num_friends_by_id, key=lambda (user_id, num_friend): num_friend, reverse=True)
# 平均一个用户的朋友关系数量
num_users = len(users)
avg_connections = total_connections / num_users
# print avg_connections
print '-----------------------------------------------------------------------------'
# 对于每一个用户的朋友们，检验这个朋友的朋友是不是这个用户的朋友
def friends_of_friend_ids_bad(user):
    return [
        foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]
        ]
print 'id, name, friend_of_friend_id'
for user in users:
    print user['id'], user['name'], friends_of_friend_ids_bad(user)
print '-----------------------------------------------------------------------------'
# 统计通过共同朋友可能成为朋友的数目
# 排除相同用户,排除已经是朋友的用户
def not_the_same(user, other_user):
    return user["id"] != other_user["id"]
def not_friends(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user["friends"])
def friends_of_friend_ids(user):
    return [
        foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]
        if not_the_same(user, foaf)
        and not_friends(user, foaf)
        ]
print 'id, name, friend_id, friend_of_friend_id'
for user in users:
    print user['id'], user['name'], [f['id'] for f in user['friends']], friends_of_friend_ids(user)
print '-----------------------------------------------------------------------------'
# 用户兴趣
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
    (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"),
    (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"),
    (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"),
    (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
    (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"),
    (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data"),
]
# 从兴趣到用户的检索
# 字典的键是兴趣，值是对该兴趣感兴趣用户名列表
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    pass
print 'interest, user_ids_by_interest'
for interest in user_ids_by_interest:
    print interest, user_ids_by_interest[interest]
    pass
# 从用户到兴趣的检索
# 键是用户名，值是该用户的兴趣列表
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    pass
print 'user_id, interests_by_user_id'
for user_id in interests_by_user_id:
    print user_id, interests_by_user_id[user_id]
    pass
print '-----------------------------------------------------------------------------'
# 对于一个特定的用户,找到和他有最多相同兴趣的用户
def most_common_interests_with(user_id):
    return [
        interested_user_id
        for interest in interests_by_user_id[user_id]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user_id
        ]
print 'user_id, common_interests_user_id, most_common_interests_user_id'
for user in users:
    print user['id'], most_common_interests_with(user['id']), Counter(most_common_interests_with(user['id']))
print '-----------------------------------------------------------------------------'
print '-----------------------------------------------------------------------------'
# 工资和经验的关系
salaries_and_tenures = [
    (83000, 8.7),
    (88000, 8.1),
    (48000, 0.7),
    (76000, 6),
    (69000, 6.5),
    (76000, 7.5),
    (60000, 2.5),
    (83000, 10),
    (48000, 1.9),
    (63000, 4.2),
]

# 不同工作年限的工资
# 键是工作年限，值是每一个工作年限的工资
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
print 'tenure, salary'
for tenure in salary_by_tenure:
    print tenure, salary_by_tenure[tenure]
# 键是工作年限，值是每一个工作年限的平均工资
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
print 'tenure, average_salary'
for tenure in average_salary_by_tenure:
    print tenure, average_salary_by_tenure[tenure]
    pass
print '-----------------------------------------------------------------------------'
# 将工作年限做一个粗略地分组再进行统计
def tenure_bucket(tenure):
    if tenure <= 2:
        return "x<=2"
    elif tenure <= 5:
        return "2<x<=5"
    else:
        return "5<x"
# 然后把属于同一个工作年限分组的工资数据合并到一个列表中
# 键是工作年限分组数据，值是该工作年限分组对应的工资列表
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    pass
print 'tenure_bucket, salary'
for tenure_bucket in salary_by_tenure_bucket:
    print tenure_bucket, salary_by_tenure_bucket[tenure_bucket]
    pass
# 对每一个工作年限分组计算平均值
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
    }
print 'tenure_bucket, average_salary'
for tenure_bucket in average_salary_by_bucket:
    print tenure_bucket, average_salary_by_bucket[tenure_bucket]
    pass
print '-----------------------------------------------------------------------------'
print '-----------------------------------------------------------------------------'
# 提取热门话题
words_and_counts = [
    word
    for user, interest in interests
    for word in interest.lower().split()
]
words_and_counts = Counter(words_and_counts)
print 'word, count'
for word, count in words_and_counts.most_common():
    print word, count
    pass
print '-----------------------------------------------------------------------------'
print '-----------------------------------------------------------------------------'
