"""
荣耀皮肤批量抓取
"""
import requests
from pyquery import PyQuery

html = requests.get('http://pvp.qq.com/web201605/herolist.shtml').content
# print(html)

# 加载html代码
doc = PyQuery(html)
items = doc('.herolist li').items()  # 查找class为herolist标签下面的li标签，空格分隔，这里的2者之间并非必须挨着，只要是层级关系即可；  涉及到id选择器和class选择器
# print(items)

for item in items:
    print(item)
    # 继续向下查找img标签的src属性
    url = item.find('img').attr('src')
    urls = 'http:' + url
    name = item.find('a').text()
    # print(url)
    img_content = requests.get(urls).content
    with open('picture/{}.jpg'.format(name), 'wb') as f:
        # 保存
        f.write(img_content)
        print('正在下载%s--------%s' % (name, urls))

print('下载完成')
