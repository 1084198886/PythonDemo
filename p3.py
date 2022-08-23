# 单行注释
'''
多行注释
'''


def MethodA(a):
    print('A')
    b = str(11)
    print(b)
    str1 = 'aaaabc#def'
    print('partition=', str1.partition('#'))
    print('replace=', str1.replace('a', 'A'))


MethodA(1)

x = 1


def changeVal(newval):
    global x
    x = newval


changeVal(2)
print(x)

list1 = [1, 2, 3]
for i in iter(list1):
    print('iter i=', i)

import hashlib

hash256 = hashlib.sha256()
srcFile = open('./p2.py', 'rb')
with srcFile as f:
    for block in iter(lambda: f.read(2048), b''):
        hash256.update(block)
    print(hash256.hexdigest())

print(ord('a'))

a, b, c = 1, 2, 3
print(a, b, c, type(a))
a, b, c = str(a), str(b), str(c)
print(a, b, c, type(a))
flag = (a, b, c) <= ('0', '5', '6')
print(flag)

print(int('122', 10))
print(True, False)

by = 'abcdef我们'.encode('utf-8')
print(by)
print(by.decode('utf-8'))
print(bytes.fromhex('b901'))

print(bool(''))

print('a', 'b', sep='')
print("%.3f" % 3.14159)

print(1 and 2)

a, b = 1, 2
result = True if a < b else False
print(result)


def mapFunc(val):
    return val + 1


lt = [1, 2, 3]
result = list(map(mapFunc, lt))
print(result)


def f1(a, *, c):
    return a + c


print(f1(1, c=2))

lt2 = [1, 2]
lt3 = lt2[:]
print('lt3=', lt3)
print('list slice eq=', lt2 == lt3)
print('is =', lt2 is lt3)

lt4 = [1] * 5
lt4[1] = 4
print(lt4)
print(6 in lt4)
print(len(lt4))


def calcmax(lt):
    if None in lt:
        print('None in list,not support calc max')
    else:
        print('max=', max(lt))


calcmax(lt4)

print("tostring:" + str(lt4))
print(sorted(lt4))
print(reversed(lt4))

lt = ["a", 2, 3, '4']
print(lt)
lt = list("abcdef")
print(lt)

rg = range(1, 5)
print(list(rg))
print(list())

lt = [1, 2]
print(lt)
lt.append(3)
print(lt)
lt.remove(1)
print(lt)
lt.extend([5, 6])
print(lt)
lt.insert(0, 1)
print(lt)
lt.pop(0)
print(lt)
lt.clear()
print(lt)
lt.append(1)
print(lt.index(1))

print(lt.count(2))

lt = tuple([1, 2])
print(lt)
a, b = lt
print(a, b)

lt = {'a': 1, 'b': 2}
print(lt)
list0 = ['a', 'b', 'c']
tuple0 = ('a', 'b', 'c')
map0 = dict.fromkeys(list0, -1)
map1 = dict.fromkeys(tuple0, -1)
print(map0)
print(map1)

lt1 = [('a', 1), ('b', 2)]
dict1 = dict(lt1)
print(dict1)
lt1 = {'a': 1, 'b': 2}
dict1 = dict(lt1)
print(dict1)

print(dict1['a'])
print(dict1.get('c', '该键不存在'))
print('a' in dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.popitem())

lt = dict.fromkeys(['a', 'b'], None)
print(lt)
ltcopy = lt.copy()
print(ltcopy)
print(ltcopy is lt)

print("A" and "a")

aa = {'a': 1, 'b': 2}
aa.update({'a': 11, 'c': 3})
print(aa)
aa.pop('a')
print(aa)
aa.popitem()
print(aa)

aa.setdefault('a', "none")
print(aa.get('a'))


def multipara(name, *args, **kwargs):
    """
    表示接收任意个数量的参数，调用时会将实际参数打包为一个元组传入实参
    :param args:
    :param kwargs:
    :return:
    """
    print(name)
    print(args)
    print(kwargs)
    # for i in args:
    #     print(i)


multipara(1, 2)
print('------------------')
multipara(1, [1, 2])
multipara(1, *[1, 2])
multipara(1, *[1, 2], **{'e': 2, 'f': 3})

lt = [1, 2, 3, 4]
st = set(lt)

lt = range(0, 4)
st = set(lt)
print(st)
st = set("abcdefg")
st.add('h')
# st.remove('k')

st.discard('h')
print(st)
# for item in st:
#     print(item)

st = frozenset(lt)
print(st)

str1 = "abcdefg  "
print(str1.startswith('a'))
print(str1.endswith('g'))
print(str1.title())
print(str1.strip())

print("I am %s" % "lilei")

s1 = 'a'
s2 = 'b'
print(f'{s1}{s2}')

print("I an {} {}".format(s1, s2))

by = b'abcdefg'
print(by.decode())

# import string
# string.ascii_lowercase

# TODO 暂未实现
if by:
    print('fsdfsd')
else:
    pass  # TODO  do nothing

print(sorted('acb'))


def my_demo(var1, var2='defval'):
    print(var1)
    print(var2)


my_demo('a1')
print(my_demo.__defaults__)
print('--------------------------------')


def build_profile(first, last, *infos, **user_info):
    print(first, last)
    print(infos)
    print(user_info)

    for key, value in user_info.items():
        print(key, ":", value)


build_profile('first:albert', 'last:einstein', "age:29", "TEL:123456", location='princeton', field='physics')

print(type(None))


class ClassA:
    pass


class TestClass:
    vara = 1

    def __init__(self, name, age: int):
        self._name = name
        self._age = age
        print(f'name={name} age={age}')

    def getname(self) -> str:
        print('getname invoked')
        return self._name

    def setname(self, name):
        self._name = name
        print('setname invoked')

    @classmethod
    def my_classmethod(self):
        print('this is my class method')

    # @property
    # def getage(self):
    #     return self._age
    #
    # @setage.setter
    # def setage(self, age):
    #     self._age = age

    @staticmethod
    def my_staticmethod():
        print('this is my static method')

    name = property(getname, setname)


testClass = TestClass('zhnagsan', 11)
# print(testClass.name + "," + str(testClass.age))
print(type(TestClass.vara))
# print(type(testClass.age))

print(testClass.getname())

TestClass.my_classmethod()

TestClass.my_staticmethod()
testClass.my_staticmethod()

print(testClass.name)
testClass.name = 'zhangsan'

# print(testClass.getage())
# print(testClass.getage)

from functools import reduce

lt = [1, 2, 3, 4, 5, 6]

sum = reduce(lambda a, b: a * b, lt)
print(f'sum={sum}')

filter1 = filter(lambda a: a % 2, lt)
print(list(filter1))

s1 = 'a b cdef   '
print(list(filter(lambda x: x and x.strip(), s1)))

s2 = 'CABb'
print(sorted(s2))
print(sorted(s2, key=str.lower))

alast = 1


def ff():
    alast = 1

    def finner():
        nonlocal alast
        return alast + 1

    return finner


f22 = ff()
print(f22())

import functools

int2 = functools.partial(int, base=2)
print(int2('0101'))


def part_func(x, y):
    print(x, y)


pt1 = functools.partial(part_func, y=1)
print('pt1=', pt1(2))

import time
import threading


def loop():
    print(f'thread {threading.current_thread().name} is running...')
    n = 0
    while n < 5:
        n = n + 1
        print(f'thread {threading.current_thread().name} >>> {n}')
        time.sleep(1)
    print(f'thread {threading.current_thread().name} ended.')


# t = threading.Thread(target=loop, name="LoopThread")
# t.start()
# t.join()
# print(f'thread {threading.current_thread().name} ended.')


class LoopThread(threading.Thread):
    def __init__(self, thread_name):
        super().__init__(name=thread_name)

    def run(self) -> None:
        loop()


loopThread = LoopThread("LoopThread")
# loopThread.start()
# loopThread.join()
print(f'thread {threading.current_thread().name} ended.')

print('-------ThreadLocal-------------')
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print(f'Hellno,{std} in {threading.current_thread().name}')


def process_thread(name):
    print(f'process_thread:{name}')
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


th1 = threading.Thread(target=process_thread, args=('AliceA',), name='Thread-A')
th2 = threading.Thread(target=process_thread, args=('AliceB',), name='Thread-B')
th1.start()
th2.start()
th1.join()
th2.join()
print('thread ended')

from multiprocessing.managers import BaseManager

print('----------datetime-------------')

from datetime import datetime, timedelta

now = datetime.now()
print(now)  # 2022-08-22 15:44:33.692142
print(datetime(2015, 4, 19, 12, 20))  # 2015-04-19 12:20:00

timestamp = now.timestamp()
print(timestamp)  # 把datetime转换为timestamp

dtime = datetime.fromtimestamp(timestamp)  # timestamp转换为datetime
print(dtime)

print(datetime.utcfromtimestamp(timestamp))

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
sday = cday.strftime('%Y-%m-%d %H:%M:%S')
print('datetime转换为str >>> ', sday)

now = datetime.now()
print(now)
delta = now + timedelta(hours=1)
print(delta)
delta = now - timedelta(hours=1)
print(delta)

from collections import namedtuple, deque, defaultdict, OrderedDict
from math import pi

Circle = namedtuple('Circle', ['x', 'y', 'r'])
p = Circle(1, 2, 4)
print(f'x={p.x}, y={p.y}, r={p.r}')

lt = [1, 2, 3, 4]
q = deque(lt)
print(q)
q.append(5)
q.pop()
print(q)
q.appendleft(-1)
q.popleft() - 1
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

dt = dict([('a', 1), ('b', 2), ('c', 3)])
print('dt=', dt)

od = OrderedDict()
od['key1'] = 'val1'
od['key2'] = 'val2'
od['key3'] = 'val3'
print(od)

from collections import ChainMap
import os, argparse

defaults = {
    'color': 'red',
    'user': 'guest',
}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
cmd_lines_args = {k: v for k, v in vars(namespace).items() if v}
print('cmd_lines_args=', cmd_lines_args)

# 组合成ChainMap:
combined = ChainMap(cmd_lines_args, os.environ, defaults)
print(f'color={combined["color"]}')
print(f'user={combined["user"]}')

from collections import Counter

import base64

enstr = base64.encodebytes(b'fsdfjds')
print(enstr)
print(base64.decodebytes(enstr))

safeenstr = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print('safe encode=', safeenstr)
print(base64.urlsafe_b64decode(safeenstr))

import struct

packb = struct.pack('>I', 10240099)
print(packb)
# print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
print(struct.unpack('>I', packb))

print(struct.pack('>s', b'abc'))

import hashlib

md5 = hashlib.md5()
md5.update('abc'.encode('utf-8'))
print('md5=',md5.hexdigest())
