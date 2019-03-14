
## 图像的RGB色彩模式

图像一般使用RGB色彩模式，即每个像素点的颜色由红R，绿G，蓝B组成。

RGB三个颜色通道之间的变化和叠加得到各种颜色，其中：
R红色，取值范围，0～255。
G绿色，取值范围，0～255。
B蓝色，取值范围，0～255。
总共叠加起来可以取：256^3种颜色。

RGB形成的颜色包括人类的视力所能感知的所有颜色。

> PIL库

PIL库是一个具有强大图像处理能力的第三方库。

安装：
```
pip install pillow
```
-----
```python
from PIL import Image
```
`Image`是PIL库中基础类，代表一个图像的类(对象)

> 图像的数组表示

计算机中，图片如何表示呢？
图像是一个由像素组成的二维矩阵，每个元素是一个RGB值。

```python
from PIL import Image
import numpy as np
import sys
import os

im = np.asarray(Image.open(os.path.join(sys.path[0], 'timg.jpg')))

print(im.shape, im.dtype) # (800, 1200, 3) uint8
# 图像是一个三维数组，维度分别是高度，宽度和像素RGB值。
```

> 图像变换

读入图像，获得像素RGB值，修改后保存为新的文件。

```python
from PIL import Image
import numpy as np

a = np.array(Image.open(''))
# 三维数组，值分别对应RGB的值。
print(a.shape, a.dtype)

b = [255, 255, 255] - a

im = Image.fromarray(b.astype('uint8'))
im.save('')
```

1. 打开图像。
2. 对RGB的值进行运算。
3. 运算后的数组，生成一个图像类型。
4. 保存文件。

```python
from PIL import Image
import numpy as np
import os
import sys

dirname = sys.path[0]

a = np.array(Image.open(os.path.join(dirname, 'timg.jpg')))
aa = np.array(Image.open(os.path.join(dirname, 'timg.jpg')).convert('L')) # convert() 将彩色的图片转换为灰度图片。
# aa 是二维数组，数值对应的是灰度值，而非RGB值。

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
```

> 手绘效果

手绘效果特征：
- 黑白灰色系
- 边界线条较重
- 相同或相近色彩趋于白色
- 略有光源(明暗五调子)

梯度重构：
利用像素之间的梯度值和虚拟深度值对图像进行重构。
根据灰度变化来模拟人类视觉的明暗程度。

```python
depth = 10. # 预设深度值为10， 取值范围0-100
grad = np.gradient(a) # 提取图片的梯度值
grad_x, grad_y = grad # 根据x和y方向的梯度值

grad_x = grad_x * depth / 100
grad_y = grad_y * depth / 100 # 根据深度调整x和y方向的梯度值
```

根据灰度变化来模拟人类视觉的远近程度:
- 设计一个位于图像斜上方的虚拟光源。
- 光源相对于图像的俯视角为Elevation, 方位角为Azimuth。
- 建立光源对于梯度值的影响函数。
- 运算出各点的新像素值。
