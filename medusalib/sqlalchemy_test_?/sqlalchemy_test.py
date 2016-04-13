#!/usr/bin/env python
# coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from models import Base, User


# 初始化数据库连接
engine = create_engine(
    'postgresql://postgres:postgres@192.168.100.100:5432/sqlalchemy',
    encoding='utf-8',
    echo=True,
)
print engine
# Engine(postgresql://postgres:***@192.168.100.100:5432/sqlalchemy)


# 创建数据表
Base.metadata.create_all(engine)
# CREATE TABLE users (
# 	id SERIAL NOT NULL,
# 	name VARCHAR,
# 	fullname VARCHAR,
# 	password VARCHAR,
# 	PRIMARY KEY (id)
# )
