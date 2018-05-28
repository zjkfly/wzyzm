# -*- coding: utf-8 -*-
"""
Created on  13:06:09 2018
判断验证码
@author: ZJKfly
"""
from PIL import Image
import math
import os

#图片矢量化
def buildvector(im):
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1


class VectorCompare:
    #计算矢量大小
    def magnitude(self,concordance):
        total = 0
        for word,count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    #计算矢量之间的 cos 值
    def relation(self,concordance1, concordance2):
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

#加载数据集
imageset =[]

for i in range(1,10):
    for letter in os.listdir('./iconset/'+str(i)):
        temp = []
        if letter != "Thumbs.db" :
            temp.append(buildvector(Image.open('./iconset/'+str(i)+'/'+letter)))
        imageset.append({i:temp})

count = 0
#对验证码图片进行余弦相似度的对比，输出结果
v = VectorCompare()

im2 = Image.open('9443.gif')
im2.convert("P")
letters = [[3,11],[15,23],[27,35],[39,47],[51,59]]
print('验证码：')
for letter in letters:
    im3 = im2.crop(( letter[0] , 0, letter[1],24 ))

    guess = []
    '''
    for image in imageset:
        for x,y in image.():
            print(x)
    '''

    for image in imageset:
        for x,y in image.items():
            if len(y) != 0:  
                guess.append( ( v.relation(y[0],buildvector(im3)),x) )
    guess.sort(reverse=True)
    print(guess[0])
    count += 1


'''
    im2 = im1.crop((3,0,11,24))
    im3 = im1.crop((15,0,23,24))
    im4 = im1.crop((27,0,35,24))
    im5 = im1.crop((39,0,47,24))
    im6 = im1.crop((51,0,59,24))
'''






