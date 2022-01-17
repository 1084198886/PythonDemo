# 单行注释
"""
多行注释，使用3个多引号
"""
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

intVal1 = input("请输入第一个int")
intVal2 = input("请输入第二个int")
ivl1 = int(intVal1)
ivl2 = int(intVal2)
sumVal = ivl1 + ivl2
print(ivl1, ivl2, "和为:", sumVal)
