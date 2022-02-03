"""
爬取电影总票房
"""
import re

import requests
from bs4 import BeautifulSoup

html = requests.get('http://58921.com/alltime').content.decode('UTF-8')
# print(html)
# 正则表达式  拿到电影名字
req = r'<td><a href="/film/.*?" title="(.*?)">.*?</a></td><td>'
title = re.findall(req, html)
# print(title)

# 源码解析
soup = BeautifulSoup(html, 'html.parser')
# 获取总票房图片
img_url = soup.find_all('img')[1:]
print(img_url)

# 遍历图片
i = 0
for url in img_url:
    # img_src = url.get('src')
    img_src = 'http://58921.com/sites/all/movie/files/cache/themes/filmt_logo.png'
    img_content = requests.get(img_src).content
    print(f'正在爬取 {title[i]}  地址:{img_src}')
    with open('result/{}.png'.format(title[i]), 'wb') as f:
        # 保存文件到目录
        f.write(img_content)
    i += 1
