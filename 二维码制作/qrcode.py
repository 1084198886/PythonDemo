"""
二维码制作
"""
import requests
from MyQR import myqr
from segno import helpers

img_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.jj20.com%2Fup%2Fallimg%2F1115%2F101021113337%2F211010113337-7-1200.jpg&refer=http%3A%2F%2Fimg.jj20.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1646406270&t=d56ec1aff5de403d301c81d1fc0caeba'
resp = requests.get(img_url)
with open('1.jpg', 'wb') as f:
    f.write(resp.content)

# 生成二维码
myqr.run(
    words='http://baidu.com',
    picture='1.jpg',
    colorized=True,
    save_name='qrcode.png',
)

# 生成个性名片，可以直接保存到联系人中
data = helpers.make_mecard(
    name='耿奇云',
    email='1084198886@qq.com',
    phone='18737165713'
)
data.save('耿奇云名片.png', scale=8)
