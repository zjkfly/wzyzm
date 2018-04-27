# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:01:33 2018
图像矢量化
@author: ZJKfly
"""
from PIL import Image
import time
import random
import math
import os

im = Image.open('1.gif')
im2 = im
d1 = {}
count = 0
for i in im.getdata():
    d1[count] = i
    count = count+1
    print(i)

d2 = dict(im2.getdata())
print(d2)