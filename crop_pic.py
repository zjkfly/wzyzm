# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 12:11:00 2018
分割图片
@author: ZJKfly
"""
import os
import random
from PIL import Image
def crop_pic(filename):
    im1 = Image.open("./pic/"+filename)
    im1.convert("P")
    im2 = im1.crop((3,0,11,24))
    im3 = im1.crop((15,0,23,24))
    im4 = im1.crop((27,0,35,24))
    im5 = im1.crop((39,0,47,24))
    im6 = im1.crop((51,0,59,24))
    im2.save("./pic/iconset1/"+str(random.randint(0,10000))+".gif")
    im3.save("./pic/iconset1/"+str(random.randint(0,10000))+".gif")
    im4.save("./pic/iconset1/"+str(random.randint(0,10000))+".gif")
    im5.save("./pic/iconset1/"+str(random.randint(0,10000))+".gif")
    im6.save("./pic/iconset1/"+str(random.randint(0,10000))+".gif")
    im2.save("./pic/iconset1/"+str(random.randint(0,10000))+".gif")
    
for i in os.listdir('./pic'):
    if i!='Thumbs.db':
        crop_pic(i)
    
    
