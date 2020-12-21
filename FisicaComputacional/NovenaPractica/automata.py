import random

from PIL import Image
from copy import deepcopy

def automata():
    images = []
    c = 1500
    img = Image.new('1', (c, c), 'white')
    imgPixels = img.load()
    # for i in range(100):
    #     for j in range(50):
    #         imgPixels[i, j]=0
    # img.save("sad.png", 'png')
    a = []
    b = []
    for i in range(c):
        aux = random.random()
        a.append(round(aux))
    j = c - 1
    while j >= 0:
        for i in range(c):
            l = i-1
            r = i+1
            if l < 0:
                l = c - 1
            if r >= c:
                r = 0
            al = a[l]
            ar = a[r]
            if al==1 and a[i]==1 and ar==1:
                b.append(0)

            if al==1 and a[i]==1 and ar==0:
                b.append(1)

            if al==1 and a[i]==0 and ar==1:
                b.append(1)

            if al==1 and a[i]==0 and ar==0:
                b.append(0)

            if al==0 and a[i]==1 and ar==1:
                b.append(1)

            if al==0 and a[i]==1 and ar==0:
                b.append(0)

            if al==0 and a[i]==0 and ar==1:
                b.append(1)

            if al==0 and a[i]==0 and ar==0:
                b.append(1)

        for k in range(c):
            if b[k]==1:
                imgPixels[k,-j] = 0
        # imgAux = deepcopy(img)
        # images.append(deepcopy(img))
        # del imgAux
        a = b
        b = []
        j = j-1
    img.save("1500.png", 'png')
    # images[0].save('pillow_imagedraw.gif',
    #            save_all=True, append_images=images[1:], optimize=False, duration=1000, loop=0)

automata()