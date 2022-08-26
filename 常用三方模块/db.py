"""
访问数据库
"""

import sqlite3

try:
    conn = sqlite3.connect('ecard_nc_dtl_db.db')
    cursor = conn.cursor()
    # cursor.execute('select * from tb_transdtl where  recno in (?,?)', (110, -1))
    # cursor.execute('select * from tb_transdtl where  recno=? and 1=1', (110,))
    # cursor.execute('select * from tb_transdtl')
    values = cursor.fetchall()  # 结果集是一个list
    # cursor.execute(r"-- insert into tb_credit_limitcnt values ('adjfksdflk',1,'20220825',1)")
    cursor.execute('create table t_user (id varchar(20) primary  key,'
                   'name varchar(20))')
    # print(values)
    print('rowcount=', cursor.rowcount)
    conn.commit()
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()

# import mysql.connector
#
# conn = mysql.connector.connect(user='root', password='password', database='test')
# cursor = conn.cursor()
#
# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#

from mymodule import *

import urllib3
import chardet
import charset_normalizer
from cryptography import __version__ as cryptography_version

print('urllib3=', urllib3.__version__)
print('chardet=', chardet.__version__)
print('charset_normalizer=', charset_normalizer.__version__)
print('cryptography_version=', list(map(int, cryptography_version.split('.'))))

print('5.0.0'.split('.')[:3])

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
print(__name__)

import sys

print(sys.version_info)

print('-------f-------------------')
IND = 'ON'


class Kls(object):
    def __init__(self, data):
        self.data = data

    @staticmethod
    def checkind():
        return IND == 'ON'

    def do_reset(self):
        if self.checkind():
            print('Reset done for:', self.data)

    def set_db(self):
        if self.checkind():
            self.db = 'New db connection'
        print('DB connection made for: ', self.data)


ik1 = Kls(12)
ik1.do_reset()
ik1.set_db()


class A(object):
    def __init__(self):
        print(A.__mro__)
        print("class ---- A ----")


class B(A):
    def __init__(self):
        print(B.__mro__)
        print("class ---- B ----")
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print(C.__mro__)
        print("class ---- C ----")
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print(D.__mro__)
        print("class ---- D ----")
        super(D, self).__init__()


d = D()

import pickle


class Test(object):
    __attrs__ = ['key1', 'key2']

    def __init__(self, v1=None, v2=None):
        print('__init__')
        self.key1 = v1
        self.key2 = v2

    def __repr__(self):
        return '{' + f'key1={self.key1},key2={self.key2}' + '}'

    def __getstate__(self):
        print(f'__getstate__')
        attrs = {}
        for attr in self.__attrs__:
            attrs[attr] = getattr(self, attr, None)
            print(f'${attr}  {attrs[attr]}')
        return attrs

    def __setstate__(self, state):
        print('__setstate__')
        # for k, v in state.items():
        #     setattr(self, k, v)
        self.key1 = '1'
        self.key2 = '2'


t = Test('zs', 11)
byte_1 = pickle.dumps(t)
print(byte_1)
s = pickle.loads(byte_1)
print(s)

redirect = bool(False) and None
print(redirect)


class CA(object):
    def __init__(self):
        print('CA __int__')

    def say(self, content):
        print('say:' + content)


def generate_obj(claz):
    print(claz)
    return claz()


obj = generate_obj(CA)
obj.say('zhangsan')

p = {'a': 1, 'b': 2}
print('a' in p)

print('AbC'.lower())
print('AbC'.upper())

from urllib.parse import urlparse, unquote

parsed = urlparse('https://www.baidu.com/s?ie=pg&wd=python&fenlei=256%65')
print(
    parsed)  # ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='ie=pg&wd=python&fenlei=256', fragment='')
print(unquote(parsed.scheme))
print(unquote(parsed.netloc))
print(unquote(parsed.query))

print(isinstance(1, (str, bytes)))


def test1(data=None, **kwargs):
    print(data)
    print(kwargs)


test1({'a': 1})

s = r'"abcde"'
print(s)
print(s.strip('\"'))

s1 = '我是中国人'.encode('utf-8')
print(s1.decode('ISO-8859-1'))
print(s1.decode('utf-8'))

from base64 import b64encode

username = 'gz'
pwd = '123456'
bstr = ':'.join((username, pwd)).strip().encode()
print(bstr)
print(b64encode(bstr))


def test_exp():
    raise ValueError('value error')


try:
    try:
        test_exp()
    except ValueError as e:
        raise
except Exception as e:
    print(e)

print('-----------map.setdefault--------------------')
mp = {}
mp['key1'] = None
# mp['key2'] = None
mp.setdefault('key2', False)
print(mp)
