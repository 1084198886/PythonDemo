""""
正则表达式
"""
import json
import re

print("match1:", re.match('www', 'www.baidu.com'))

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

print("search:", re.search('www', 'www.baidu.com').group())

# json
data = {'no': 1, 'name': 'Runoob', 'url': 'http://www.runoob.com'}
json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)

data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])
