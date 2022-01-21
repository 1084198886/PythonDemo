"""
文件操作
"""
import os
from time import time

# 写文件
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
