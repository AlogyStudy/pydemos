
import json
import os
import sys
import time

import numpy as np
from PIL import Image


'''
# 原理：利用像素之间的梯度值和虚拟深度值对图像进行重构，根据灰度变化来模拟人类视觉的模拟程度
Image.open() # 打开图片
np.asarray() # 将图像转化为数组
convet('L') # 将图片转换为二维灰度图片
Image.fromarray() # 将数组还原成图像uint8格式
'''

def image (sta, end, depths = 10):
    a = np.asarray(Image.open(sta).convert('L')).astype('float')
    depth = depths  # 深度的取值范围(0-100)，标准取10
    grad = np.gradient(a)  # 取图像灰度的梯度值
    grad_x, grad_y = grad  # 分别取横纵图像梯度值
    grad_x = grad_x * depth / 100. # 对grad_x值进行归一化
    grad_y = grad_y * depth / 100. # 对grad_y值进行归一化

    A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / A
    uni_y = grad_y / A
    uni_z = 1. / A

    vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
    vec_az = np.pi / 4.  # 光源的方位角度，弧度值

    dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
    dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
    dz = np.sin(vec_el)  # 光源对z 轴的影响
    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
    b = b.clip(0, 255)
    im = Image.fromarray(b.astype('uint8'))  # 重构图像
    im.save(end)

def main ():
    xs = 10
    start_time = time.clock()
    try:
        startss = os.listdir(sys.path[0])
        time.sleep(2)
        for starts in startss:
            start = ''.join(starts)
            sta = os.path.join(sys.path[0], start)
            end = os.path.join(sys.path[0], 'HD_' + start)
            image(sta=sta, end=end, depths=xs)
    except OSError as identifier:
        pass
    end_time = time.clock()
    print('程序运行：'+ str(end_time - start_time) + ' 秒')
    time.sleep(3)

if __name__ == '__main__':
    main()
