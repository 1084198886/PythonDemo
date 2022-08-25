import chardet

byte = '离离原上草，一岁一枯荣'.encode('gbk')
ret = chardet.detect(byte)
print(ret)
encoding = ret.get('encoding')
print(encoding)
dc = byte.decode(encoding)
print(dc)
