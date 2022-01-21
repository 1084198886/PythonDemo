"""
爬虫demo
"""

import csv  # 用于把爬取的数据存储为csv格式，可以excel直接打开的
import time  # 用于对请求加延时，爬取速度太快容易被反爬
from time import sleep  # 同上
import random  # 用于对延时设置随机数，尽量模拟人的行为
import requests  # 用于向网站发送请求
from lxml import etree  # lxml为第三方网页解析库，强大且速度快

url = 'http://yz.yuzhuprice.com:8003/findPriceByName.jspx?page.curPage=1&priceName=%E7%BA%A2%E6%9C%A8%E7%B1%BB'
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/81.0.4044.129 Safari/537.36",
}
response = requests.get(url, headers=headers, timeout=10)
# requests.post(url,data=dict(key1="value1"))
html = response.text
print(html)

parse = etree.HTML(html)  # 解析网页
all_tr = parse.xpath('//*[@id="173200"]')  # 每一行数据对应源码里的一个id=173200的tr，那就先把这些tr都提取下来
for tr in all_tr:
    tr = {
        'name': ''.join(tr.xpath('./td[1]/text()')).strip(),
        'price': ''.join(tr.xpath('./td[2]/text()')).strip(),
        'unit': ''.join(tr.xpath('./td[3]/text()')).strip(),
        'supermaket': ''.join(tr.xpath('./td[4]/text()')).strip(),
        'time': ''.join(tr.xpath('./td[5]/text()')).strip()
    }
print(tr)

with open('wood.csv', 'a', encoding='utf_8_sig', newline='') as fp:
    # 'a'为追加模式（添加）
    # utf_8_sig格式导出csv不乱码
    fieldnames = ['name', 'price', 'unit', 'supermaket', 'time']
    writer = csv.DictWriter(fp, fieldnames)
    writer.writerow(tr)
