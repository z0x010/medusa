#!/usr/bin/env python
# coding:utf-8


DATABASE = 'postgresql://postgres:postgres@192.168.100.100:5432/sqlalchemy'

print '----------------------------------------------------------------------------------------------------'
"""
Connecting
"""

from sqlalchemy import create_engine

engine = create_engine(
    DATABASE,
    encoding='utf-8',
    echo=True,
)
print engine
# Engine(postgresql://postgres:***@192.168.100.100:5432/sqlalchemy)
print '----------------------------------------------------------------------------------------------------'
"""
Declare a Mapping
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence

Base = declarative_base()
print type(Base)
# <class 'sqlalchemy.ext.declarative.api.DeclarativeMeta'>
print Base
# <class 'sqlalchemy.ext.declarative.api.Base'>

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __repr__(self):
        return "<User(id=%s, name='%s', fullname='%s', password='%s')>" % (self.id, self.name, self.fullname, self.password)
print '----------------------------------------------------------------------------------------------------'
"""
Create a Schema
"""

Base.metadata.create_all(engine)

# CREATE TABLE users (
# 	id INTEGER NOT NULL,
# 	name VARCHAR(50),
# 	fullname VARCHAR(50),
# 	password VARCHAR(12),
# 	PRIMARY KEY (id)
# )

#              Table "public.users"
#   Column  |         Type          | Modifiers
# ----------+-----------------------+-----------
#  id       | integer               | not null
#  name     | character varying(50) |
#  fullname | character varying(50) |
#  password | character varying(12) |
# Indexes:
#     "users_pkey" PRIMARY KEY, btree (id)
print '----------------------------------------------------------------------------------------------------'
"""
Create an Instance of the Mapped Class
"""

import random

def rand_user():
    name = ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)) + (''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))).lower()
    fullname = name + ' ' + ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)) + (''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))).lower()
    password = (''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 6)))
    user = User(
        name=name,
        fullname=fullname,
        password=password,
    )
    return user

print rand_user()
# <User(id=None, name='Atcqr', fullname='Atcqr Fkezt', password='4R3XEY')>
print '----------------------------------------------------------------------------------------------------'
"""
Creating a Session
"""

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
print type(Session)
# <class 'sqlalchemy.orm.session.sessionmaker'>
print Session
# sessionmaker(
#     class_='Session',
#     autoflush=True,
#     bind=Engine(postgresql://postgres:***@192.168.100.100:5432/sqlalchemy),
#     autocommit=False,
#     expire_on_commit=True,
# )
session = Session()
print session
# <sqlalchemy.orm.session.Session object at 0x10b38e310>
print '----------------------------------------------------------------------------------------------------'
"""
Adding and Updating Objects
"""

user = rand_user()
print user
# <User(id=None, name='Dlfrp', fullname='Dlfrp Cwxjg', password='KPAVF1')>

session.add(user)
session.commit()
# BEGIN (implicit)
# INSERT INTO users (id, name, fullname, password) VALUES (nextval('user_id_seq'), %(name)s, %(fullname)s, %(password)s) RETURNING users.id
# {'fullname': 'Bruce Wayne', 'password': 'batman', 'name': 'bruce'}
# COMMIT

print user
# BEGIN (implicit)
# SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
# FROM users
# WHERE users.id = %(param_1)s

# <User(id=31, name='Dlfrp', fullname='Dlfrp Cwxjg', password='KPAVF1')>

print user in session
# True
print '----------------------------------------------------------------------------------------------------'
"""
Rolling Back
"""

user = rand_user()
print user
# <User(id=None, name='Uoeax', fullname='Uoeax Wcpkf', password='KTXP96')>

session.add(user)
session.rollback()
# ROLLBACK

print user
# <User(id=None, name='Uoeax', fullname='Uoeax Wcpkf', password='KTXP96')>

print user in session
# False
print '----------------------------------------------------------------------------------------------------'
"""
Querying
(order_by)
"""

users = session.query(User).order_by(User.id)
print type(users)
# <class 'sqlalchemy.orm.query.Query'>
print users
# SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
# FROM users ORDER BY users.id

for instance in users:
    print instance

# <User(id=30, name='Mrlef', fullname='Mrlef Sksan', password='J97WV2')>
# <User(id=31, name='Dlfrp', fullname='Dlfrp Cwxjg', password='KPAVF1')>
# <User(id=32, name='Vdkro', fullname='Vdkro Msjza', password='GUL7PJ')>
# <User(id=33, name='Pnkis', fullname='Pnkis Hdorn', password='L7AK12')>
print '----------------------------------------------------------------------------------------------------'
"""
Querying
(filter)
"""
users = session.query(User).filter(User.name.like('A%'))
print type(users)
# <class 'sqlalchemy.orm.query.Query'>
print users
# SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password
# FROM users
# WHERE users.name LIKE :name_1

for instance in users:
    print instance

# <User(id=44, name='Anamt', fullname='Anamt Utwfg', password='064U9B')>
# <User(id=88, name='Axiah', fullname='Axiah Rpwkr', password='JQVAXB')>
print '----------------------------------------------------------------------------------------------------'
"""
Querying
(others)
"""

print session.query(User).filter(User.name.like('A%')).all()
# [<User(id=44, name='Anamt', fullname='Anamt Utwfg', password='064U9B')>,
#  <User(id=88, name='Axiah', fullname='Axiah Rpwkr', password='JQVAXB')>]

print session.query(User).filter(User.name.like('A%')).count()
# 2

print session.query(User).filter(User.name.like('A%')).first()
# <User(id=44, name='Anamt', fullname='Anamt Utwfg', password='064U9B')>

print session.query(User).filter(User.name.like('An%')).one()
# <User(id=44, name='Anamt', fullname='Anamt Utwfg', password='064U9B')>

# print session.query(User).filter(User.name.like('A%')).one()
# sqlalchemy.orm.exc.MultipleResultsFound

print session.query(User).filter(User.name.like('An%')).one_or_none()
# <User(id=44, name='Anamt', fullname='Anamt Utwfg', password='064U9B')>

print session.query(User).filter(User.name.like('Anx%')).one_or_none()
# None

print '----------------------------------------------------------------------------------------------------'
