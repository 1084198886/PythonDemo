""""
类测试
"""
import string


class A:
    def __init__(self, reason, filename=None):
        print("A __init__ reason=%s filename:%s " % (reason, filename))
        self.reason = reason
        if filename is not None:
            self.filename = filename
            print("A start filename define")

    @property
    def reason(self):
        return self.reason

    @reason.setter
    def reason(self, reason):
        self.reason = reason

    def __str__(self):
        return '<A reason= %s >' % self.reason


class B:
    def __init__(self, reason, filename=None):
        print("B __init__ reason=%s filename:%s " % (reason, filename))
        self.reason = reason
        if filename is not None:
            self.filename = filename
            print("B start filename define")


class C(A, B):
    """"
    构造器中调用父类构造器方法
    """

    def __init__(self, message, content):
        # super().__init__(message)
        A.__init__(self, message)
        # B.__init__(self, message)
        # super(A, self).__init__(message)  # 用子类对象调用父类已被覆盖的方法
        self.content = content
        print("C __init__")


# b = C("C-message", "C-content")
# a = A("A para")
# print(a.reason)

def _noop(obj):
    return obj


tuple1 = (1, 2, '')
tuple2 = (2, 3)
print(tuple1 + (_noop,))
print(tuple(x + 2 if x else x + str(3) for x in tuple1))  # tuple元组的生成

a, b = tuple2
print('a=%d b=%d ' % (a, b))

print('partition : ', "www.runoob.com".partition('.'))  # partition :  ('www', '.', 'runoob.com')
print('rpartition : ', "www.runoob.com".rpartition('.'))  # rpartition :  ('www.runoob', '.', 'com')

print(int('E122', 16))
print(int('EF', 16))
print("replace用法  ", "abc".replace("a", "A"))
print(string.ascii_lowercase)

lt1 = [4, 1, 2, 3]
lt2 = ['a', 'b']
print(dict([x for x in zip(lt1, lt2)]))
print([x for x in reversed(lt1)])
print([x for x in sorted(lt1)])

tuple3 = (3, 4, 5)
print('%d.%d', tuple3[:2])


# 关键字参数
def keywordpara(url, *, timeout, name):
    print(url, timeout)


keywordpara("http:/", timeout=1, name=1)

print("1" == 1)
if not "":
    print("falg1----")
else:
    print("flag2---")

strr1 = "FFF|ff"
strr1.split()
print(strr1)


def opentest(req):
    if isinstance(req, str):
        print("req is istanace of str")
    else:
        print("req type is %s" % type(req))


opentest("I'am a string")
opentest(UnboundLocalError())

lt = [1, 2, 3]

# for block in iter(lambda: f.read(4096), b''):  # TODO

for i in iter(lt):
    print("iter=", i)

