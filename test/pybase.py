# 单行注释
"""
多行注释，使用3个多引号
"""
import time

'''
多行注释，使用3个单引号
'''
import keyword

print("Python教程：http://c.biancheng.net/python/")
a = 10
b = 20
print(a * b)
print(keyword.kwlist)
print(abs(-199))

flag = True
str1 = "A"
str2 = "B"
result = str1 + str2
print("result=" + result)

print(type(8888888888888888888888))  # <class 'int'>
print(type(-7777777777777777777777))  # <class 'int'>
print(type("1"))  # <class 'str'>
print(type(True))  # <class 'bool'>

num1 = 122_222_222_2
num2 = 12.1_2
print("1_222_22=" + str(num1) + ",    12.1_2=" + str(num2))  # 数字分隔符使用

cp = 12 + 0.2j
print(cp)
print(type(cp))

s1 = "I\" an a big beg"
print("字符串中出现引号的处理:  " + s1)
num3 = "AAAAAAAAAAAAAAAAAA" \
       "AAAAAAAAAAAAAAAAAAAAA"
print("字符串换行[行尾添加反斜杠\]=" + str(num3))

longstr = '''it took me a few minutes to get the bool.do you know?
JFSJFLKJSLFJLSKDFJSLKFJK""LD""SJ
FLSJFKJDKFLJKS'''
print("长字符串=" + longstr)

origstr = r'I\'am great! D\:\Program Files\Python 3.8\python.exe'
print("原始字符串=" + origstr)

'''
bytes类型及用法
'''
b1 = b''
b2 = bytes()
b3 = bytes('http://c.biancheng.net/python/', encoding='UTF-8')
b4 = b'http://c.biancheng.net/python/'
b5 = "abc语言中文网8岁了".encode("UTF-8")
print("b4:", b4)
print("b4[3]:", b4[3])
print("b4[7:22]:", b4[7 - 22])
print("b5:", b5)

s4 = b4.decode("UTF-8")  # bytes对象转换为字符串
print("s4=", s4)

'''
python bool布尔类型
'''
t1 = True
t2 = t1 + 1
print("t2=", t2)

# intVal1 = input("请输入第一个int")
# intVal2 = input("请输入第二个int")
# ivl1 = int(intVal1)
# ivl2 = int(intVal2)
# sumVal = ivl1 + ivl2
# print(ivl1, ivl2, "和为:", sumVal)

'''
print()函数高级用法
'''
print("a", "b")  # 输出多个值
print("a", "b", sep="#", end=" ")  # sep 改变默认分隔符  end改变末尾自动换行标记
f = open("demo.txt", mode='w')
print("only test python print file attribute", file=f)
print()
f.close()

'''
格式化字符串
'''
print("%s已经%d岁了！" % ("张三", 10))
print("url(35):%35s" % "http://c.biancheng.net/python/")  # 指定最小输出宽度
print("int(5):%5d" % 2)  # 指定最小输出宽度

print("int(5):%05d" % 2)  # 表示宽度不足时补充 0，而不是补充空格
print("int(5):%-5d" % 2)  # 指定位数不足时左对齐
print("int(5):%+5d" % 2)  # 表示输出的数字总要带着符号；正数带+，负数带-

print("%.3f" % 3.141592653)  # 指定小数精度

'''
转移字符
'''
print("转义字符：%s" % "\061\062\063")  # 转义字符：123
print("转义字符：%s" % "Hex: \x31\x32\x33\x78\x79\x7A")  # 转义字符：Hex: 123xyz

'''
数据类型转换
'''
a = int("1")

print("乘法运算符:", "a" * 5)

print("/运算符:", 5.0 / 2)
print("//运算符:", 5.0 // 2)
print("%运算符:", 5.0 % 2)
print("**次方运算符:", 5 ** 2)

a = b = c = 9
print("连续赋值运算符 %d,%d,%d:" % (a, b, c))
a += 2
print("+=运算符:%d" % a)

t1 = time.gmtime()
t2 = time.gmtime()
print("== 和 is 的区别:%s" % (t1 is t2))

'''
逻辑运算符
'''
a = 1
b = 2
c = a and b
print("c=", c)

'''
三目运算符
'''
a = 1
b = 1
print('a>b' if a > b else ('a<b' if a < b else 'a==b'))

'''
list
'''
lt = [None] * 5
print(lt)
str = "c.biancheng.net"
seq = [1, 2, 3, 4]
print("c是否在", str, "中：", 'f' in str, sep="")
print("c是否不在", str, "中：", 'f' not in str, sep="")
print("len(str):", len(str))
print("max(str):", max(str))
print("min(str):", min(str))
print("sorted(str):", sorted(str))
print("sum(str):", sum(seq))

lt2 = ["http://c.biancheng.net/python/", 1, [2, 3, 4], 3.0]
lt3 = []
lt4 = list("abc")
print("abc转换为list:", lt4)
tuple1 = ('a', 'b', 'c')
print("元组转换为list:", list(tuple1))

dict1 = {'a': 100, 'b': 42, 'c': 9}
print("dict转换为list:", list(dict1))
range1 = range(1, 6)
print("range转换为list:", list(range1))
# del lt2  #删除list
lt3.append("a")  # append添加元素
lt3.append(('JavaScript', 'C#', 'Go'))  # append添加元组
print("lt3:", lt3)
print("lt3[1]:", lt3[1])
lt5 = [1, 2]
lt5.extend([3, 4])
print("lt5=", lt5)
print("lt5[2]=", lt5[2])

lt6 = [1, 2]
lt6.insert(1, [3, 4])
print("lt6=", lt6)
del lt6[0]
print("lt6删除第0个元素后=", lt6)
del lt6[0:1]
print("lt6删除第0,1个元素后=", lt6)
lt7 = [1, 2, 3, 4, 5, 6]
lt7.pop(0)  # 根据索引值删除元素
print("lt7.pop(0)后=", lt7)
lt7.remove(2)  # 根据元素值进行删除
print("lt7.remove(2)后=", lt7)
lt7.clear()
print("lt7.clear()后=", lt7)

'''
修改元素
'''
lt8 = [1, 2, 3]
lt8[0] = 11
print("lt8修改第0个元素后=", lt8)

lt8[0:2] = [-1, -2]
print("lt8修改第0,1个元素后=", lt8)

lt9 = [1, 2, 3, 4, 5]
print("元素3的位置是：", lt9.index(3))
print("元素3的位置是：", lt9.index(3, 2, len(lt9)))

tuple2 = (1, 2, 3)

'''
dict字典
'''
dict2 = {'数学': 95, '英语': 92, '语文': 84}
print("dict2=", dict2)

list10 = ['数学', '英语', '语文']
scores = dict.fromkeys(list10, 60)
print("fromkeys创建dict:", scores)

list11 = [('数学', 95), ('英语', 92)]
dict3 = dict(list11)
print("dict()方式创建dict:", dict3)
print("dict3.get()查询：", dict3.get('数学', '该键不存在!'))
dic4 = {'key1': 1, 'key2': 2}
dic4['key3'] = 3
print("dict插入元素：", dic4)
dic4['key3'] = -3
print("dict修改元素：", dic4)
del dic4['key3']
print("dict删除元素：", dic4)
print("dict4是否存在key1：", 'key1' in dic4)
print("dict4是否不存在key1：", 'key1' not in dic4)

'''
dir(dict)
'''
print("dir(dict): ", dir(dict))

dic5 = {'key1': 1, 'key2': [1, 2, 3]}
print("dic.keys=", list(dic5.keys()))
print("dic.values=", list(dic5.values()))
print("dic.items=", dic5.items())

for k in dic5.keys():
    print(k, end=" ")
print("\n---------------")
for v in dic5.values():
    print(v, end=" ")
    print("\n---------------")
for k, v in dic5.items():
    print('key:', k, ' value:', v)
dic5_copy = dic5.copy()
dic5['key3'] = 3
print("添加key3 后 dict5:", dic5)
print("添加key3 后  copy dict5:", dic5_copy)
dic5['key2'].remove(1)  #
print("删除key2下面的浅拷贝数据后 dict5:", dic5)
print("删除key2下面的浅拷贝数据后 copy dict5:", dic5_copy)

dic5.update({'key1': 2, 'key4': 'value4'})
print("update dict5后：", dic5)

dic5.pop('key4')
print("pop dict5[key4]后：", dic5)
dic5.popitem()
print("popitem dict5后：", dic5)

dic5.setdefault('key5', 'none')

'''
set集合
'''
set1 = {1, 1, 2, 4, (1, 2, 3)}
print("set1=", set1)
set2 = set((1, 2, 3))
print("set2=", set2)
set3 = set("abcdefg")
print("set3=", set3)
# set3.remove('h')  # h不存在时，会抛出KeyError错误
set3.discard('h')  # h不存在时，不会抛出KeyError错误
print("remove a 后 set3=", set3)

set01 = {1, 2}
set02 = {2, 3}
print("交集:", set01 & set02)
print("并集:", set01 | set02)
print("差集:", set01 - set02)  # 取一个集合中另一集合没有的元素
print("对称差集:", set01 ^ set02)  # 取集合 A 和 B 中不属于 A&B 的元素

set01.add(3)
# set01.remove(4)
set01.clear()
set01.copy()
set01.difference(set02)
set01.difference_update(set02)
set01.discard(1)
set01.issubset(set02)
# set01.pop()
set01.union(set02)
set01.update(set02)
'''
frozenset  不可变集合
'''
set03 = frozenset(['Java', 'Shell'])

barray = bytearray('aaaa', encoding="UTF-8")
# barray.insert(0, 'b')
# barray.extend('ab')
# barray.pop(1)
# barray.remove(3)
# barray.clear()
# barray.reverse()
print(len(barray))
print('decode result:', barray.decode())

print("a|b|c".split("|"))

bts = bytes()
hexstr = bts.fromhex("B9 01EF")
print(hexstr)
print(bytes.fromhex('B9 01EF'))

lst = ['a', 'b', 'c']
print('/'.join(lst))

ba = bytearray()
ba.append(65)
print(ba.decode())
