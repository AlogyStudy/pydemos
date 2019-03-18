## pydemos
py demos


项目：
- `handDrawn`, 将图片转手绘。
- `friendsHeadStitch`, 微信个人号接口，统计用户，头像拼接。
- `pi`, 计算π值大小。
- `GPS`, GPS定位

## python库

`print(dir(modules))` 查看内置模块
`pip list` 查看已经安装模块

> 内置库

- `import time/import datetime`
- `import sys`
- `import os`
- `import re`
- `import math`
- `import random`
- `import json`
-----
- `import base64`
- `import uuid`
- `import hashlib`
- `import functools`
- `import fileinput`

> 第三方库

- `from PIL from Image`
- `import numpy as np`
- `import pandas`
- `import itchat` 微信
- `import django`
- `import scrapy`
- `import pymysql`


> numpy

numpy系统是Python的一种开源的数值计算扩展
- 存储和处理大型矩阵
- 用Python实现的科学计算包
    强大的N维数组对象
    成熟的函数库
    实用的线性代数，傅立叶变换和随机数的生成函数
- 提供很多高级的数值编程工具
    矩阵数据类型
    矢量处理
    精密的运算库

基本知识：
`Numpy`的主要对象是同种元素的多维数组。
维度(`dimensions`)叫做轴(`axes`)
轴的个数叫做秩(`rank`)
例如：在3D空间一个点的坐标[1, 2, 3]是一个秩为1的数组，因为它的只有一个轴，轴长度为3。

`Numpy`的数组类被称之为ndarray,叫做：数组。

创建数组：
- 使用array函数，利用Python列表和元祖创造数组。所创建的类型由原序列中的元素类型决定。
- 使用占位符创建数组：`np.zeros()`, `np.one()`, `np.empty()`创建一个内容随机并且依赖内存状态的数组。
- `arange()`函数来返回数组。

基本运算：
- 数组的算术运算是按元素进行，`Numpy`中的乘法运算符`*`按元素个数。
- 矩阵乘法使用`dot()`



