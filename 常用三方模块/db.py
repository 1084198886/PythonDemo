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

print(all([True, None]))

s = '1'
s += '2'
print(s)
s = 1
s += 1
print(s)

print(6 / 3)

import hashlib


def md5(bs):
    md5str = hashlib.md5(bs).hexdigest()
    print('md5:' + md5str)
    return hex


import time
import os

print(md5('abcdefg1'.encode('utf-8')))
print(time.ctime().encode('utf-8'))

by = os.urandom(8)
print(by)
base = 'ffffffffffffffffffffffffffffffffffffff' \
       'fffffffffffff'

print(sys.version_info)

import copy

lt = [1, [1, 2]]
c = copy.copy(lt)
print(lt == c)
c = copy.deepcopy(lt)
print(lt == c)


def tuple_test():
    return 1, 2


print(tuple_test())  # (1, 2)


def getNoSameItems(domains):
    lst = []
    for item in domains:
        if item is not None and item not in lst:
            lst.append(item)
    print(lst)


ret = getNoSameItems([1, 1, 4, 6, 7, 7, None, ''])
print(ret)  # [1, 4, 6, 7]

print('--------------------')
o = [1, [3, 4]]
c = copy.deepcopy(o)
id0 = id(o)
id1 = id(c)
print(o, '   ', c)
print(f'id0={id0}   id1={id1}  {id0 == id1}')

o.append(6)
print(o, '   ', c)
o[1].append(5)
print(o, '   ', c)

result = {
    'version': 1,
    'rfc2109': False,
}
print(set(result))
print(set({'version': 2, 'rfc2109': False, 'a': 1}) - set(result))

print(time.time())

import calendar

print(calendar.calendar(2022))

morsel = {'expires': '%Y:%m:%d %H:%M:%S'}
time_template = '%a, %d-%b-%Y %H:%M:%S GMT'
expires = calendar.timegm(time.gmtime())
g = time.gmtime()
print(g)
print(expires)

import sys

try:
    flag = sys.version_info == '1.1'
    if flag:
        raise Exception('error occured')
    print('success')
except Exception as e:
    print('error happended:' + repr(e))
else:
    print('fdsfs')

import platform

print(platform.python_implementation())
print(platform.python_version())
print(platform.python_version_tuple())
print(platform.platform())
print(platform.version())
print(platform.architecture())
print(platform.uname())


class Info:
    def __init__(self):
        self.stuempno = '1202020'
        self.name = 'zhangsan'

    def __bool__(self):
        print('__bool__ 调用了')
        return False

    @property
    def my_stu(self):
        return self.stuempno

    def __call__(self, *args, **kwargs):
        print('__call__:  ', args)


info = Info()
print(info.my_stu)
print(info(1, 2, 2))
print('bool(info)=', bool(info))


class A(dict):
    def __call__(self, *args, **kwargs):
        print(args)


class B(list):
    def __call__(self, *args, **kwargs):
        print(args)


i = (A, B)
print(hasattr(A, '__call__'))
print(hasattr(B, '__call__'))
if hasattr(i, '__call__'):
    infos = [i]
    print(infos)

from urllib.parse import urlsplit, urlencode

print('urlsplit:', urlsplit('https://baidu.com/home/a?a=1&b=2'))
print('urlparse:', urlparse('https://baidu.com/home/a?a=1&b=2'))

v = vars(info)
print(v, type(v))
print(v.items())
print(v.get('stuempno'))

print(urlencode({'a': 1, 'b': 2}))
print(urlencode([('a', 1), ('b', 2)]))

mp = {'a': 1, 'b': 2}
it = mp.items()
print(list(it))

A = [1, 2]
A.extend([3, 4])
A.extend((5, 6))
print(A)

mp = {'a': None, 'b': 1, 'c': '', 'd': 2}
none_keys = [k for k, v in mp.items() if not v]
for key in none_keys:
    del mp[key]
print(mp)

from urllib.parse import urljoin

print(urljoin('http://baidu.com', 'home/fsd'))


def genera():
    for i in range(5):
        yield i * i


g = genera()
print(next(g))
print(next(g))
print(next(g))

print('http://baidu.com'.startswith(('http', 'b')))

import zipfile

zip = zipfile.ZipFile('zipf.zip', 'w', zipfile.ZIP_DEFLATED)
zip.write('good_09.png')
zip.write('pillow.py')
for zname in zip.namelist():
    print(zname)
for zname in zip.infolist():
    print(zname)
zip.close()

import tempfile

print(tempfile.gettempdir())
print(os.path.join(tempfile.gettempdir(), 'ff'))
print(os.path.exists(tempfile.gettempdir() + '/f'))

print(sys.version_info)

# emp_file = tempfile.mkstemp(dir='.')
# print(emp_file)

fd = os.open('pillow.py', os.O_RDWR)
print(fd)
# os.fdopen()

item = [1, 2, 3, 4]
print(item[:1])
print(item[-2:])
print(item[1:-1])

a = 2
if a != 2:
    print('a!=2')


def method1(mname):
    def m1(age):
        print(f'{mname}  {age}')

    return m1


method1('a')('b')


def loop():
    for n in range(5):
        yield n


ge = loop()
nex = next(ge)
print(nex)
print(sys.maxunicode)

import codecs

t = codecs.lookup('utf-8')
print((t[0], t[1]))
print(t[2], t[3])

# import  csv
# reader = codecs.getreader('utf-8')
# textstream = reader([1,3])
# csv.DictReader(textstream)
# writer = codecs.getwriter('utf-8')
# encoder = codecs.getencoder('utf-8')
# decoder = codecs.getdecoder('utf-8')

import struct
import socket

ip = '192.168.1.1'
struct.pack('')
ipaddr = struct.unpack('=L', socket.inet_aton(ip))[0]
print(ipaddr)

a = 12
bts = struct.pack('i', a)
print(bts)
s = struct.unpack('i', bts)
print(s)
