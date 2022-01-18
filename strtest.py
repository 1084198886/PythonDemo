'''
字符串操作
'''

# repr, encode,str
import sys
from functools import partial

s = "abc"
s_str = str(s)
s_repr = repr(s)  # repr会返回python 表达式的形式
print(s_str)
print(s_repr)

s1 = "人生苦短，我用Python"
ec = s1.encode(encoding="UTF-8")
print("len获取字节数:", len(ec))

# split
s3 = "A|BCD|E"
splitstr = s3.split("|")
print("split用法:", splitstr)
for item in splitstr:
    print(item)

# join
s4 = ('usr', 'usr', 'bin', 'env')  # tuple 元组类型
s4_ret = '/'.join(s4)
print("join的用法：", s4_ret)
print("join的用法：", ','.join("ABCD"))
# count()
print("字符串中usr出现的次数：", s4.count('usr'))

# find()  index
s5 = "  Mary wrote an article on why the team had failed to win the game! That's end !  "
pos = s5.find("article")
rpos = s5.rfind("article")
print("find查找子串的索引：", pos)
idx = s5.index("article")  # 不存在时会抛异常
ridx = s5.rindex("article")  # 从右边开始检索
print("index查找子串的索引：", idx)
print("startWith()方法：", s5.startswith("Mary"))
print("endswith()方法：", s5.endswith("!"))
print("title方法将字符串的每个单词的首字母转为大写：", s5.title())
print("lower方法将字符串中的所有大写字母转换为小写：", s5.lower())
print("upper方法将字符串中的所有小写字母转换为大写：", s5.upper())

print("删除字符串左右两边的空格和特殊字符[不包含中间的]：", s5.strip())
print("删除字符串左侧的空格和特殊字符[不包含中间的]：", s5.lstrip())
print("删除字符串右侧的空格和特殊字符[不包含中间的]：", s5.rstrip())

strweb = "网站名称：{:>9s}\t网址：{:s}"
print(strweb.format("C语言中文网", "c.biancheng.net"))

# 以货币形式显示
print("货币形式：{:,d}".format(1000000))
# 科学计数法表示
print("科学计数法：{:E}".format(1200.12))
# 以十六进制表示
print("100的十六进制：{:#x}".format(100))
# 输出百分比形式
print("0.01的百分比表示：{:.0%}".format(0.01))

# encode decode
str1 = "encode test"
ecstr = str1.encode("UTF-8")
# print("encode 编码字符串：", ecstr)
dcstr = ecstr.decode("UTF-8")
print("decode解码字符串：", dcstr)

print(str(1))

# if elif else
# height = float(input("输入身高（米）："))
height = float(11.5)
if height < 18.5:
    if height >= 10:
        print("体重为：", height)
    elif height > 5:
        # TODO:暂未实现
        pass  # 空语句 pass  用来让解释器跳过此处，什么都不做
    else:
        print("体重过轻")
elif 18.5 <= height < 29.9:
    print("正常范围，注意保持")
else:
    print("肥胖")

# while循环
str2 = "zhangsan"
i = 0
while i < len(str2):
    print(str2[i])
    i += 1
print("while循环结束!")

# for
sum = 0
for i in range(101):
    sum += i
print("计算 1+2+...+100 的结果为：", sum, sep="")
# 迭代list，tuple
my_list = [1, 2, 3, 4, 5]
for ele in my_list:
    print('ele =', ele)

# 遍历字典
my_dic = {'python教程': "http://c.biancheng.net/python/",
          'shell教程': "http://c.biancheng.net/shell/",
          'java教程': "http://c.biancheng.net/java/"}
for dictkey in my_dic:
    print('dictkey =', dictkey)
for dictvalue in my_dic.values():
    print('dictvalue =', dictvalue)
for items in my_dic.items():
    print('items =', items)

# while结束后else代码块
lt1 = [1, 2, 3]
i = 0
while i < len(my_list):
    print("while  ", my_list[i])
    i += 1
else:
    print("while执行完成，执行else")

# for结束后else代码块
for dictvalue in my_dic.values():
    print("dict value:", dictvalue)
else:
    print("for执行完毕，执行else")

# break 跳出循环
add = "http://c.biancheng.net/python/,http://c.biancheng.net/shell/"
# 提前定义一个 bool 变量，并为其赋初值
flag = False
for i in range(3):
    for j in add:
        if j == ',':
            # 在 break 前，修改 flag 的值
            flag = True
            break
        print(j, end="")
    print("\n跳出内循环")
    # 在外层循环体中再次使用 break
    if flag:
        print("跳出外层循环")
        break

# continue用法
for i in add:
    if i == ',':
        # 忽略本次循环的剩下语句
        print('\n')
        continue
    print(i, end="")

lt3 = [1, 2, 3]
dtl = dict.fromkeys(lt3, -1)
print(dtl)

# zip
my_list2 = [1, 2, 3]
my_tuple = ('a', 'b', 'c', 'd')
zp = zip(my_list2, my_tuple)
# for zi in zp:
#     print("zip item:", zi)

print([x for x in zp])

# reversed
print("reversed 序列：", [x for x in reversed([1, 2, 3, 4, 5])])
print("reversed 元组：", [x for x in reversed((1, 2, 3, 4, 5))])
print("reversed 字符串：", [x for x in reversed("abcdefg")])
print("reversed range(5)：", [x for x in reversed(range(5))])
print("reversed list(reversed(5))：", list(reversed(range(5))))

# sorted 排序
print("序列升序排序：", sorted([1, 9, 6, 2]))
print("序列降序排序：", sorted([1, 9, 6, 2], reverse=True))
print("元组排序：", sorted((1, 9, 6, 2)))
print("字典排序：", sorted({"key1": 1, "key3": 3, "key2": 2}))
print("字符串排序：", sorted("cba"))
print("key 指定 sorted() 函数按照什么标准进行排序：", sorted(["c", "aaaaaa", "bbb"], key=lambda x: len(x)))


# def 函数
def my_func1():
    pass


def str_max(str1, str2):
    '''
     我是函数注释
    :param str1: 字符串1
    :param str2: 字符串1
    :return: 返回最大值
    '''
    maxstr = str1 if str1 > str2 else str2
    return maxstr


print("str_max(1,2)", str_max(str1=1, str2=2))
print("str_max(abc,de)", str_max("abc", "de"))
print(str.__doc__)


# 形参和实参 值传递和引用传递
def demo(f):
    f += f
    print("形参值为：", f)


print("-------值传递-----")
a = "abc"
demo(f=a)
print("实参值：", a)
print("-------引用传递-----")

a = ['a', 'b', 'c']
demo(f=a)  # 关键字参数
print("实参值：", a)


# 默认值参数

def default_para(para1, para2="default para2"):
    print("para1=" + para1, "para2=" + para2)
    return 0


print("默认值参数:", default_para("a"))
print("打印默认参数值:", default_para.__defaults__)


# 可变参数
def make_pizza(size, *toppings):
    """
    打印顾客点的所有配料
    :param toppings:
    :return:
    """
    print(size)
    print(toppings)


make_pizza(10, 'pepperoni')
make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')

print("print返回值是否是None:", print() is None)


# 函数返回多个值
def hours_to_write(happy_hours):
    week1 = happy_hours + 2
    week2 = happy_hours + 4
    week3 = happy_hours + 6
    return [week1, week2, week3]


print("函数返回多个值 list: ", hours_to_write(4))


def people_age():
    d = dict()
    d['Jack'] = 30
    d['Kim'] = 28
    d['Bob'] = 27
    return d


d = people_age()
print("函数返回多个值 dict: ", d)


def natural_numbers(numbers=[]):
    for i in range(1, 16):
        numbers.append(i)
    return numbers


print(natural_numbers())


class Intro:
    def __init__(self):
        self.str1 = "hello"
        self.str2 = "world"

    def __str__(self):
        print("call self str func")


def message():
    return Intro()


x = message()
print("x.str1=", x.str1, ",x.str2=", x.str2)

'''
偏函数partial
'''


# 定义个原函数
def display(name, age):
    print("name:", name, "age:", age)


# 定义偏函数，其封装了 display() 函数，并为 name 参数设置了默认参数
GaryFun = partial(display, name='Gary')
# 由于 name 参数已经有默认值，因此调用偏函数时，可以不指定
GaryFun(age=13)
