from PIL import Image
import numpy as np
import sys
import os

# im = np.asarray(Image.open(os.path.join(sys.path[0], 'timg.jpg')))

# print(im.shape, im.dtype) # (800, 1200, 3) uint8

dirname = sys.path[0]

a = np.array(Image.open(os.path.join(dirname, 'timg.jpg')))
aa = np.array(Image.open(os.path.join(dirname, 'timg.jpg')).convert('L'))

b = [255, 255, 255] - a
c = 255 - aa # 灰度值取反
d = (100 / 255) * aa + 150 # 区间变换, a 乘 100 后除以，当前灰度值做一个区间压缩，再 加上150，扩充区间范围。
e = 255 * (aa / 255) ** 2  # 像素的平方

imb = Image.fromarray(b.astype('uint8'))
imb.save(os.path.join(dirname, 'timgb.jpg'))

imc = Image.fromarray(c.astype('uint8'))
imc.save(os.path.join(dirname, 'timgc.jpg'))

imd = Image.fromarray(d.astype('uint8'))
imd.save(os.path.join(dirname, 'timgd.jpg'))

ime = Image.fromarray(e.astype('uint8'))
ime.save(os.path.join(dirname, 'timge.jpg'))
