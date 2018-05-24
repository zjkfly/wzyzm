# -*- coding: utf-8 -*-
"""
Created on 11:25:43 2018
download image
@author: ZJKfly
"""
import requests
import random
url = "http://wzjw.sdwz.cn/ImageValidate.ashx?temp=jggmc5og"
r =requests.get(url)
filename = str(random.randint(0,10000))+".gif"
f= open(filename,'wb')
f.write(r.content)
f.close()

#批量下载图片文件并写入文本

url = "http://wzjw.sdwz.cn/ImageValidate.ashx?temp=jggmc5og"
r =requests.get(url)
filename = str(random.randint(0,10000))+".gif"
f= open(filename,'wb')
f.write(r.content)
f.close()
url = "http://wzjw.sdwz.cn/ImageValidate.ashx?temp=jggmc5og"
r =requests.get(url)
filename = str(random.randint(0,10000))+".gif"
f= open(filename,'wb')
f.write(r.content)
f.close()
url = "http://wzjw.sdwz.cn/ImageValidate.ashx?temp=jggmc5og"
r =requests.get(url)
filename = str(random.randint(0,10000))+".gif"
f= open(filename,'wb')
f.write(r.content)
f.close()
