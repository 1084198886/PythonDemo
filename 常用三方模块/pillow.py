"""
pillow图像处理
"""
import math

from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
img = Image.open('good_09.png')
# 获得图像尺寸:
w, h = img.size
print(f'w={w}  h={h}')
# 缩放到50%:
img.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
img.save('thumbnail.jpg', 'jpeg')
