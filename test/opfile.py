"""
文件操作
"""
import os
import pickle
import urllib
from time import time

# 写文件
from urllib.request import urlopen

import requests
from lxml import etree

try:
    file = open(file="write.txt", encoding="UTF-8", mode="w+")  # w--覆盖模式  a--追加模式
    print(f"name={file.name} mode={file.mode} encoding={file.encoding} closed={file.closed}")
    file.write("我是第一行\n我是第二行\n")
    file.writelines(["item1", "item2"])
finally:
    file.close()

# os.remove("demo.txt")

# 读文件
file = open(file="write.txt", encoding="UTF-8", mode="r+")
# print("read()读取文件：\n", file.read())
print("readline()读取一行文件：\n", file.readline())
file.close()

# 读取多行
try:
    file = open(file="write.txt", encoding="UTF-8", mode="r+")
    print("readlines()读取一行文件：\n", file.readlines())
except:
    pass
finally:
    file.close()

with open(file='demo.txt', encoding="utf-8", mode='w+') as f:
    f.write("open file using with\n")
    f.writelines("a new line")

# pickle模块
tup1 = ('I love Python', {1, 2, 3}, None)


class TupleClas:
    age = 10
    name = "zhangsan"


tupclas = TupleClas()
by1obj = pickle.dumps(tup1)
print("pickle.dumps: ", by1obj)
byobj = pickle.dumps(tupclas)
print("pickle.dumps: ", byobj)

print("pickle.loads: ", pickle.loads(by1obj))
obj2 = pickle.loads(byobj)
print("pickle.loads: ", obj2)
# print("pickle.loads: ", TupleClas(obj2))


# with open("fileobj.txt", mode="w+") as f:
# pickle.dump(tup1, f)
# print("pickle.loads: ", )

response = requests.get("https://baidu.com")
print("response: ", response.text)
html = etree.HTML(response.text)
print("html:", html)

ltdir = os.listdir()
print(ltdir)
if 'mydir' not in ltdir:
    print("mydir not exist, start create")
    os.mkdir("mydir")
os.chdir('mydir')

if 'subdir' not in os.listdir():
    print("subdir not exist, start create")
    os.mkdir('subdir')

os.chdir('subdir')
with open('subfile.txt', 'w+', encoding="UTF-8") as f:
    f.write("写入了一个中文1222!")
