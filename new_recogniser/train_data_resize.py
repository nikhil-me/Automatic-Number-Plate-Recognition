from multiprocessing import Pool
from PIL import Image
import os
import os.path




#p=Pool(5)

def process_fpath(path):
    #listing=os.listdir(path)
    #im=Image.open(path1+path)
    inc=1

    im=Image.open(path)
    im=im.convert('L')
    imw=im.size[0]
    imh=im.size[1]
    pix=im.load()
    start=0
    flag=0
    end=0
    flag1=0
    flag2=0
    flag3=0
    left=128
    right=0
    for i in range(1,imh):
       for j in range(1,imw):
          if (pix[i,j]!=255):
             flag=1
          if (flag==1):
             start=i
             break
       
    for i in range(imh-1,-1,-1):
       for j in range(1,imw):
           if (pix[i,j]!=255):
              flag1=1
           if (flag1==1):
              end=i
              break
       
    for i in range(1,imh):
       flag2=0
       for j in range(1,imw):
           if (pix[i,j]!=255):
              flag2=1
           if (flag2==1):
              left=min(left,j)
              break
                  
    for i in range(imh-1,-1,-1):
        flag3=0
        for j in range(1,imw):
           if (pix[i,j]!=255):
              flag3=1
           if (flag3==1):
              right=max(right,j)
              break
    box=(left,start-10,right+5,end+10)
    area=im.crop(box)
    area.show()
    im.resize((28,28),Image.ANTIALIAS)
    #im1=im.copy()
    #loc=os.path.join('/home/nikhil/n/imp/btp/testimages/newimages/',inc+".jpg")
    #im1.save(loc)
    #inc=inc+1
    im.show()
    #print start
    #print inc
    #im.save(os.path.join(path2,path), "JPEG")

process_fpath('img.bmp')         
