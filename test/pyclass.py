"""
python类和对象
"""

# 类定义
import logging
import os
import sys
import time
import traceback
from abc import abstractmethod
from enum import Enum, unique

from urllib3._collections import RLock


class TheFirstDemo:
    """
    这是一个学习Python定义的第一个类
    """
    # 下面定义了一个类属性
    add = 'http://c.biancheng.net'

    def __init__(self, name, age):
        # 下面定义 2 个实例变量
        self.name = name
        self.age = age
        print("构造器调用了")

    # 下面定义了一个say方法
    def say(self, content):
        print("say方法调用了，content=", content)


demo = TheFirstDemo("zhangsan", 20)
demo.say("say a word !")
print("name=%s age=%d" % (demo.name, demo.age))

demo.stuempno = "00001"  # 对象动态添加属性
print("stuempno=%s" % demo.stuempno)
del demo.stuempno  # 对象动态删除属性


# print("stuempno=%s" % demo.stuempno)  # 此时会报AttributeError

# 动态添加方法
def info(self):
    print("__info__函数")


demo.foo = info  # 使用info对clanguage的foo方法赋值（动态绑定方法）
demo.foo(demo)  # Python不会自动将调用者绑定到第一个参数，因此程序需要手动将调用者绑定为第一个参数
demo.bar = lambda self: print("__lambda表达式__")
demo.bar(demo)


# 创建空类
class Empty:
    pass


# 类变量和类方法
class CLanguage:
    # 下面定义了2个类变量
    name = "C语言中文网"
    add = "http://c.biancheng.net"

    def __init__(self):
        self.stuempno = "00001"  # 示例变量

    # 下面定义了一个say实例方法
    def say(self, content):
        count = 0.8 * 22  # 局部变量
        print("say: ", content, count, self)

    @classmethod
    def dosomething(cls):  # 类方法
        print("do something ", cls)

    @staticmethod
    def mystaticmethd():
        print("static方法调用")


print("---------修改类变量的值 会影响到所有的实例----------")
cl1 = CLanguage()
cl2 = CLanguage()
print("修改name前:cl1.name=%s      cl2.name=%s" % (cl1.name, cl2.name))
CLanguage.name = "newname"
print("修改name后:cl1.name=%s      cl2.name=%s" % (cl1.name, cl2.name))
cl1.say("hello")
print("---------修改1个实例变量的值 不会影响到所有的实例----------")

print("修改name前:cl1.stuempno=%s      cl2.stuempno=%s" % (cl1.stuempno, cl2.stuempno))
cl1.stuempno = "new0001"
print("修改name后:cl1.stuempno=%s      cl2.stuempno=%s" % (cl1.stuempno, cl2.stuempno))
'可以看到，只有cl1变量的 stuempno字段发生了变化'

# 类方法
CLanguage.dosomething()

# 静态方法
CLanguage.mystaticmethd()
cl1.mystaticmethd()


# 类命名空间
class Item:
    print("正在定义Item类")
    for i in range(10):
        if i % 2 == 0:
            print("偶数")
        else:
            print("奇数")

    def foo(self):
        print("foo")


global_fn = lambda p: print('执行lambda表达式，p参数: ', p)


class Category:
    cate_fn = lambda p: print('执行lambda表达式，p参数: ', p)


# 调用全局范围内的global_fn，为参数p传入参数值
global_fn('fkit')
c = Category()
# 调用类命名空间内的cate_fn，Python自动绑定第一个参数
c.cate_fn()


class DescribeFlag:
    s = "abc"

    def __init__(self, name):
        self.name = name
        print("__init__ 定义实例变量:%s" % name)

    def __get__(self, instance, owner):
        print("call __get__", self, instance)
        return self.name

    def __set__(self, instance, value):
        print("call __set__", self, instance)
        self.name = value


# 描述符类
class revealAccess:
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val

    def __set__(self, obj, val):
        print("updating", self.name)
        self.val = val


class myClass:
    x = revealAccess(10, 'var "x"')
    y = 5


m = myClass()
print(m.x)
m.x = 20
print(m.x)
print(m.y)


class CLanguage2:
    def __init__(self, n):
        self.__name = n

    # 设置 name 属性值的函数
    def setname(self, n):
        self.__name = n

    # 访问nema属性值的函数
    def getname(self):
        return self.__name

    # 删除name属性值的函数
    def delname(self):
        self.__name = "xxx"

    # 为name 属性配置 property() 函数
    name = property(fget=getname, fset=setname, fdel=delname)


# 调取说明文档的 2 种方式
# print(CLanguage.name.__doc__)
help(CLanguage2.name)
clang = CLanguage2("C语言中文网")
# 调用 getname() 方法
print(clang.name)
# 调用 setname() 方法
clang.name = "Python教程"
print(clang.name)
# 调用 delname() 方法
del clang.name
print(clang.name)


class Rect:
    def __init__(self, area):
        self.__area = area

    @property  # property装饰器，可以直接通过方法名来访问方法
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    @area.deleter
    def area(self):
        self.__area = 0


rect = Rect(8)
print("area is:%d" % rect.area)
rect.area = 1  # 配置了@area.setter后 就可以直接赋值了。
print("修改后 的 area is:%d" % rect.area)
del rect.area
print("删除后 的 area is:%d" % rect.area)


# 类的封装

class UserInfo:
    def setuname(self, uname):
        if len(uname) < 3:
            raise ValueError("名称长度必须大于3！")
        else:
            self.__uname = uname

    def getuname(self):
        return self.__uname

    # 为 name 配置 setter 和 getter 方法
    uname = property(fget=getuname, fset=setuname)

    def setaddr(self, addr):
        if addr.startswith("http://"):
            self.__addr = addr
        else:
            raise ValueError("地址必须以 http:// 开头")

    def getaddr(self):
        return self.__addr

    # 定义个私有方法
    def __display(self):
        print(self.__uname, self.__addr)

    addr = property(fget=getaddr, fset=setaddr)


userInfo = UserInfo()
userInfo.uname = "zhangsan"
userInfo.addr = "http://c.biancheng.net"
print(userInfo.uname, userInfo.addr)

# 私有方法的调用
# userInfo._UserInfo__display()

print("继承演示......")


# 继承
class People:
    def say(self):
        print("people say")


class Animal(object):  # 默认继承object类
    def say(self):
        print("animal say")

    def eat(self):
        print("Animal eat")

    def display(self):
        print("animal display")

    def __show(self):
        print("show")


class Person(Animal, People):
    pass

    def eat(self):
        print("Person eat")


p = Person()
p.say()
p.display()
p.eat()

Animal.eat(p)


# 子类的使用

class NewDictError(ValueError):
    """如果向NewDict 添加重复值，则引发此异常"""


class NewDict(dict):
    """
    新建dict子类
    :param dict:
    :return:
    """

    def __setitem__(self, key, value):
        """不接受重复值的字典"""
        if value in self.values():
            """
              if (key in self and self[key] != value) or (key not in self):
                  raise NewDictError("这个值已经存在，并对应不同的键")
            """
        super().__setitem__(key, value)


newDict = NewDict()
newDict["key1"] = "value1"
print(newDict)
newDict["key2"] = "value1"
print(newDict)


class People2:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("我是人，名字为：", self.name)


class Animal2:
    def __init__(self, food):
        self.food = food

    def display(self):
        print("我是动物,我吃", self.food)


class Person2(People2, Animal2):
    def __init__(self, name, food):
        # 调用 People2 类的构造方法
        super().__init__(name)
        # People.__init__(self,name) #使用未绑定方法调用 People 类构造方法
        # 调用其它父类的构造方法，需手动给 self 传值
        Animal2.__init__(self, food)


per = Person2("zhangsan", "熟食")
per.say()
per.display()


# 多态
class WhoSay:
    def say(self, who):
        who.say()


class GoLang:
    def say(self):
        print("GoLang say")


class CLang:
    def say(self):
        print("CLang say")


whoSay = WhoSay()
whoSay.say(GoLang())
whoSay.say(CLang())


# 枚举

@unique  # python 默认允许enum中有相同的值，添加@unique后，可以禁止相同
class Color(Enum):
    """为序列值指定value值"""
    red = 1
    yellow = 2
    green = 3


print("red  name=%s  value=%s" % (Color.red.name, Color.red.value))

for color in Color:
    print("遍历： name=%s  value=%s" % (color.name, color.value))
print([("k=%s" % color.name, "v=%d" % color.value) for color in Color])

for name, member in Color.__members__.items():
    print("k2=%s  v2=%s" % (name, member))

# Enum构造器创建枚举：

em = Enum("EnumClas", ('E1', 'E2'))
for e in em:
    print(e)


class SpecialCls:
    name = "zhangsan"
    age = 10

    def __init__(self):
        print("call SpecialCls.__init__")

    def __new__(cls, *args, **kwargs):
        print("call SpecialCls.__new__:", cls, args, kwargs)
        return super().__new__(cls)

    def __repr__(self):
        # super().__repr__(self)
        return "name=%s  age=%d" % (self.name, self.age)

    def __del__(self):
        print("call SpecialCls.__del__:")

    def say(self):
        print("say")


special = SpecialCls()
special.say()
print("重写__repr__后直接打印SpecialCls对象：", special)
del special

# dir用法
print(dir(str))


#  __dict__用法
class ParentClas:
    class_attr1 = "class_attr1_val1"
    class_attr2 = "class_attr1_val2"

    def __init__(self):
        self.obj_attr1 = "obj_attr1_val"
        self.obj_attr2 = "obj_attr2_val"


class SubClas(ParentClas):
    pass


dictClas = ParentClas()
print("使用__dict__查询类变量：", ParentClas.__dict__)
print("使用__dict__查询示例变量：", dictClas.__dict__)  # 注意：要在对象上调用

# setattr  getattr   hasattr
print("setattr 用法：", getattr(dictClas, "class_attr1"))
print("setattr 用法：", getattr(dictClas, "obj_attr1"))

setattr(dictClas, "stuempno", "0001")
print("setattr 后  stuempno：", getattr(dictClas, "stuempno"))
print("hasattr 用法：", hasattr(dictClas, "class_attr1"))

dicSubClas = SubClas()
print("issubclass 用法：", issubclass(SubClas, (ParentClas, object)))
print("isinstance 用法：", isinstance(dicSubClas, SubClas))

print("__bases__输出类所有的直接父类组成的元组：", SubClas.__base__)
print("__bases__输出类所有的直接父类组成的元组：", ParentClas.__base__)


class A:
    def __init__(self):
        print("A __init__")

    def __call__(self, name, age):
        print("name=%s age=%d" % (name, age))


a = A()
a("zhangsan", 10)


# 运算符重载
class OverideFuc:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name:%s ;age:%d" % (self.name, self.age)

    __repr__ = __str__  # 转化为供解释器读取的形式

    def __lt__(self, other):  # 重载 self<record 运算符
        if self.age < other.age:
            return True
        else:
            return False

    def __add__(self, other):  # 重载 + 号运算符
        return OverideFuc(self.name, self.age + other.age)


myc = OverideFuc("Anna", 42)  # 实例化一个对象 Anna，并为其初始化
mycl = OverideFuc("Gary", 23)  # 实例化一个对象 Gary，并为其初始化
print(repr(myc))
print(myc)
print(str(myc))
print(myc < mycl)
print(myc + mycl + mycl)

# 函数装饰器
print("函数装饰器------------")


def funA(fn):
    print("funA：")

    # 定义一个嵌套函数
    def say(*args, **kwargs):
        fn(*args, **kwargs)

    return say


@funA
def funB(arc):
    print("C语言中文网：", arc)


@funA
def other_funB(name, arc):
    print(name, arc)


funB("http://c.biancheng.net")
other_funB("Python教程：", "http://c.biancheng.net/python")

# 异常处理机制

try:
    print(2 / 1)
    # raise KeyError("FSFSF")
except (ZeroDivisionError, ValueError) as ex:
    # print("args err1:   ", ex.args)
    # print("str err2:   ", str(ex))
    # print("repr err2:   ", repr(ex))  # 建议使用repr
    # traceback.print_tb(ex)  # 使用traceback打印更加详细的异常信息
    # print(sys.exc_info())
    traceback.print_exc()

except Exception as ex:
    print("未知异常:  %s" % ex)

finally:
    print("I'am finally clause")


class InputError(Exception):
    """当输入有误时抛出此异常"""

    def __init__(self, value):
        self.value = value

    # 返回异常类对象的说明信息
    def __str__(self):
        return ("{} is invalid input".format(repr(self.value)))


try:
    raise InputError(1)  # 抛出 MyInputError 这个异常
except InputError as err:
    print('error: {}'.format(err))

print("start learning logging")
# logging 使用
filePath = '../output/filename.log'
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(filename)s [%(lineno)d] %(threadName)s : %(message)s',
                    datefmt='[%Y-%b-%d %H:%M:%S]')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler(filename=filePath, encoding="UTF-8", mode="a"))
logger.info("write an English name")
logger.info("写入一段中文")


# file = open("../output/test.log", "w")
# file.write("FSFSFDS")
# file.close()

def capitalize(content):
    """首字母的小写转大写"""
    x = content[0]
    if 'a' <= x <= 'z':
        ch = chr(int(ord(x) - 32))
        print(f"{ch}{content[1:]}")  # 以 f开头表示在字符串内支持大括号内的python 表达式


capitalize("abc")

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for fl in myFiles:
    print(os.path.join('C:\\demo\\exercise', fl))

print("当前工作目录： ", os.getcwd())
# os.chdir("E:\\pyspace\\PythonDemo")  # 切换工作目录
print("getcwd： ", os.getcwd())
print("abspath： ", os.path.abspath("."))
print("isabs： ", os.path.isabs("e:\\pyspace"))
print("relpath： ", os.path.relpath("e:\\pyspace\\PythonDemo", "e:\\"))
print("dirname： ", os.path.dirname("e:\\pyspace\\PythonDemo"))
# time.sleep(1)
print("basename： ", os.path.basename("e:\\pyspace\\PythonDemo"))


class ErrNotFound:
    """我是一个类"""


# 断言
try:
    assert 1 > 2
except AssertionError as ex:
    print("assrt err:  ", repr(ex))
finally:
    print("fjdslfkjsdlkfj")

p1, p2, p3 = 1, 2, 3
print(p1, p2, p3)
p1, p2, p3 = str(p1), str(p2), str(p3)
print(p1, p2, p3)

q1, q2, q3 = 1, 2, 3
flag = (1, 2, 3) <= (q1, q2, q3) < (2, 3, 4)
print(f"flag={flag}")

# map
mp = list(map(float, ["1", "2", "3"]))
print(f"map={mp}")  # map=[1.0, 2.0, 3.0]


def mapFunc(val):
    return val * 2


mp2 = list(map(mapFunc, [1, 2, 3]))
print(f"mp2={mp2}")  # mp2=[2, 4, 6]

print("{}|{}|{}".format(1, 2, 3))  # 1|2|3


# from sys import (argv as a, abiflags as b)


class PersonV:
    def __init__(self):
        self.age = 10
        print("PersonV __init__")


class Student(PersonV):
    """
    :param
    """

    def __init__(self, name):
        super().__init__()
        print(f"Student __init__,name={name}")


stu = Student("zhangsan")
print(f"age={stu.age}")


class AttrTest:
    __attrs__ = ['max_retries', 'config', '_pool_connections']

    def __init__(self):
        self.max_retries = "max_retries"
        self.config = 2
        self._pool_connections = 5

    def __getstate__(self):
        return {attr: getattr(self, attr, None) for attr in self.__attrs__}

    @property
    def pool_connections(self):
        return self._pool_connections


attr = AttrTest()
print(f"max_retries={attr.max_retries}  config={attr.config}  _pool_connections={attr.pool_connections}")
# 说明：因为_pool_connections属性开头有_,是受保护的，为了便于其它模块访问，定义pool_connections方法，并注解即可

if True and False:
    print("true")
else:
    print("False")

print(str("a"))
print(repr("a"))
print(len('aaaa'))


# __slots__用法

class SlotTest(object):
    # __slots__ = ("method1", "sayA")

    def __init__(self):
        self.method1 = "ffff"

    def sayA(self) -> str:
        return 'sayA method has bean invoked '

    def sell_fruit(self, flag: float) -> str:
        print("sell_fruit")
        return 'I\'am selling fruit !'


st = SlotTest()
print(st.method1)
print(st.sayA())
st.sell_fruit(1)

print('{arg1}|{arg2}'.format(arg1=1, arg2=2))

dict2 = dict({1: 1, 2: 2})


class ClsC:
    pass


from abc import ABCMeta


class ClsA:

    def __init__(self):
        self.a = 2
        print("A init")

    # @abstractmethod
    # def say(self, para: ClsC):
    #     pass
    # print("A say  ", para)


class ClsB(ClsA):
    clas_a = ClsA
    cls_b = ClsA()
    cls_c: ClsA = {}


a = ClsA()
clsB = ClsB()
# print("clas_a=", clsB.clas_a.say("@#$"))
print("clas_a 类型=", type(clsB.clas_a))
print("clas_b 类型=", type(clsB.cls_b))
print("clas_c 类型=", type(clsB.cls_c))


class Payment(metaclass=ABCMeta):  # 其中metaclass=ABCMeta是必需的

    @abstractmethod  # 调用@abstractmethod规定子类必须有pay方法，否则会报错
    def pay(self, money):
        pass

    @abstractmethod
    def pay2(self):
        pass

    @abstractmethod
    def pay3(self):
        pass

    @abstractmethod
    def pay4(self):
        pass


class Wechatpay(Payment):
    def pay4(self):
        pass

    def pay(self, money):
        pass

    def pay2(self):
        pass

    def pay3(self):
        pass


print(os.path.join("a", 'b'))

file = open('demo.txt', mode='w')
file.write('1\n')
file.writelines('2\n')
file.writelines(['3\n', '4'])
file.close()
time.sleep(0.5)

file = open('demo.txt', mode='r')
lines = file.readlines()
for line in lines:
    print(line)

print('ord()用法：', ord('a'))
print('chr()用法：', chr(99))
print('hex()用法：', hex(99))

s = r'"我是原始字符串"\n'
print(s)


class T1:
    def __init__(self, name):
        print("T1 init:", type(name))

    def __call__(self, *args, **kwargs):
        print(args)
        return 0


class T2:
    def __init__(self, name):
        print("T2 init:", type(name))


t1 = T1('zhangsan')
doc = t1('a', 'b')
doc2 = t1.__call__('a', 'b')
