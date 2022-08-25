import chardet

byte = '离离原上草，一岁一枯荣'.encode('gbk')
ret = chardet.detect(byte)
print(ret)
encoding = ret.get('encoding')
print(encoding)
dc = byte.decode(encoding)
print(dc)

import requests

r = requests.get('https://baidu.com')
content = r.content
print(r.text)

encoding = chardet.detect(content).get('encoding')
print('html ecoding: ', encoding)  # utf-8
print(content.decode(encoding))
