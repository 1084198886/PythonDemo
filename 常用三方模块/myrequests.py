import requests

r = requests.get('https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448')
print(r.status_code)
# print(r.text)

# 带参
para = {'q': 'python', 'cat': '1001'}
r = requests.get('https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448',
                 params=para)
print(r.url)
print(r.status_code)
print(r.encoding)
# print(r.text)
# print(r.json())

r = requests.get('https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)

# r = requests.post('https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448',
#                   data={'a': 1, 'b': 2})
# print(r.text)

# r = requests.post('https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448',
#                   json={'a': 1, 'b': 2})
# print(r.text)

r = requests.post('https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448',
                  files={'file': open('good_09.png', 'rb')})
# print(r.text)
# print(r.headers)
# print(r.cookies['ts'])

r = requests.get('https://www.baidu.com', cookies={'token': '12345'}, timeout=2.5)
print(r.text)
