"""
这里是模块说明文档
"""
import string
import sys

from test import module1 as md1
from test import module1
# from test2 import module3 as t2
# import test2.module3 as md3

name = "zhangsan in module1"
age = 10

md1.hide_func()

if __name__ == '__main__':
    print("this is module1_test __main__ :%s " % __name__)
    print("module1=", module1)
    print("type(module1)=", type(module1))
    md1.say()
    cl = md1.CLanguage("zhangsna", "add")
    cl.say()
    # t2.say()
    # md3.say()
    print(cl)
    print("当前模块说明:", __doc__)
    print("sys.path:", sys.path)

    # print("dir查看模块成员=", dir(t2))
    print("查看模块特殊成员=", [d for d in dir(string) if not d.startswith("_")])
    print(module1.__file__)
    # print(t2.__file__)
    print(string.__file__)
else:
    print("this is not module1_test __main__ :%s " % __name__)
