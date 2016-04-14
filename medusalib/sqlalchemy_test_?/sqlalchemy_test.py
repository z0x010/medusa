#!/usr/bin/env python
# coding:utf-8


print '----------------------------------------------------------------------------------------------------'
"""
Connecting
"""

from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://postgres:postgres@192.168.100.100:5432/sqlalchemy',
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

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)
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

my_user = User(name='bruce', fullname='Bruce Wayne', password='batman')
print '----------------------------------------------------------------------------------------------------'
"""
Creating a Session
"""

from sqlalchemy.orm import sessionmaker

session_maker = sessionmaker(bind=engine)
print session_maker
# sessionmaker(
#     class_='Session',
#     autoflush=True,
#     bind=Engine(postgresql://postgres:***@192.168.100.100:5432/sqlalchemy),
#     autocommit=False,
#     expire_on_commit=True,
# )
session = session_maker()
print session
# <sqlalchemy.orm.session.Session object at 0x106366ad0>
print '----------------------------------------------------------------------------------------------------'
"""
Adding and Updating Objects
"""

session.add(my_user)
session.commit()
# BEGIN (implicit)
# INSERT INTO users (id, name, fullname, password) VALUES (nextval('user_id_seq'), %(name)s, %(fullname)s, %(password)s) RETURNING users.id
# {'fullname': 'Bruce Wayne', 'password': 'batman', 'name': 'bruce'}
# COMMIT
print '----------------------------------------------------------------------------------------------------'
"""
Rolling Back
"""

ex_user = User(name='clark', fullname='Clark Kent', password='superman')
session.add(ex_user)
session.rollback()
print '----------------------------------------------------------------------------------------------------'
"""
Querying
"""

users = session.query(User).order_by(User.id)
for instance in users:
    print instance

# <User(name='bruce', fullname='Bruce Wayne', password='batman')>
# <User(name='clark', fullname='Clark Kent', password='superman')>
print '----------------------------------------------------------------------------------------------------'
"""
Querying (?)
"""
print '----------------------------------------------------------------------------------------------------'
