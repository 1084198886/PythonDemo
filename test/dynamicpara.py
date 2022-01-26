""""
动态参数
Python的动态参数有两种，分别是*args和**kwargs.默认大家都使用*args和**kwargs
"""


def func(*args):
    """
    *表示接收任意个数量的参数，调用时会将实际参数打包为一个元组传入实参
    """
    print(args)

    for i in args:
        print(i)


func('name', ['a', 'b'])
func('name', *['a', 'b'])  # 加一个*号，表示将列表中的每个元素作为单独的参数传递进去

print("---------------------------")


def func(*args):
    """
    *表示接收任意个数量的参数，调用时会将实际参数打包为一个元组传入实参
    """
    for i in args:
        print(i)


func(123, 'hello', ['a', 'b', 'c'], *{'name': 'kobe', 'age': 41})

print("----------------------------------")


def func(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)


func("zhangsan", *[1, 2, 3], **{'key1': 1, 'key2': 2})
