from PIL import Image
import ImageEnhance
import ImageFilter
import ImageOps,ImageChops
import scipy
import numpy as np
from scipy import ndimage
from scipy.misc import imsave
from numpy import ndarray
import matplotlib.pyplot as plt
from sobel import sobel
import trial2
from regiongrow import Rgrow
import time

'''Notations used
   imw= image width
   imh= image height
   im.size[0] gives width of image
   im.size[1] gives height of image
'''

#function to darken the horizontal strip from pixel y1 to y2
def darkenHStrip(img,y1,y2):
 imn=img.copy()
 imw=img.size[0]
 for i in range(y1,y2):
   for j in range(1,imw):
     imn.putpixel((j,i),0)
 imn.show()




def Resize(img , bw):
 wpercent = (bw/ float(img.size[0]))
 hsize = int((float(img.size[1]) * float(wpercent)))
 img = img.resize((bw, hsize), Image.ANTIALIAS)
 return img

#binarization of image using global thresholding
def GBinarization(im):
  imw= im.size[0]
  imh= im.size[1]
  print imw
  print imh
  hs=im.histogram()
  th=0
  pix=im.load()
  for i in range(len(hs)):
   th+=i*int(hs[i])
  th=th/(imw*imh)
  th=50
  for i in range(imh):
    for j in range(imw):
        if pix[j,i]<th :
           im.putpixel((j,i),0)
  return im


#binarization of image using Local thresholding
def LBinarization(im):
  imw= im.size[0]
  imh= im.size[1]
  pix=im.load()
  winw=3
  winh=3
  x=0 
  y=0
  while(x <= (imh-winh)):
    print x
    y=0
    while(y<= (imw-winw)):
         th=0
         for i in range(x,x+winh):
            for j in range(y,y+winw):
               th+= pix[j,i]
         th=th/(winw*winh)
         #th=max(0,th-30) 
         for i in range(x,x+winh):
            for j in range(y,y+winw):
               if pix[j,i]<(th-10):
                  im.putpixel((j,i),0)
               else:
                  im.putpixel((j,i),255)
         y+=winw
    x+=winh
  return im 

def PreProcess(im):
   im=NMode(im)
   im1 = ndimage.grey_erosion(im, size=(10,10))
   scipy.misc.imsave("eroded.jpg",im1)
   im1= Image.open("eroded.jpg")
 
   im=ImageOps.equalize(im,0)
   im=ImageChops.difference(im1, im)
   #print ("image height %d and width %d\n"%(imh,imw))
 
 
   im=GBinarization(im)#binarize the image
   return im

#Processing the image
def Process(i):
 src="EXE/"+str(i)+".JPG"
 im = Image.open(src)
 im=Resize(im,400)
 im=im.convert('L') #converts image into grayscale
 imp=im.copy()
 im.show()
 im=PreProcess(im)
 #im.show()

 Y=trial2.DetermineY(im)
 maxm=0
 max_j=0
 #trial2.Plot(Y)
 
 for i in range(150,im.size[1]):
      if( Y[i]>maxm ):
           maxm=Y[i]
           max_j=i
 #print "------"
 #print max_j
 im,top,bottom=Rgrow(im,150,max_j)  
 #im.show()
 
 box = (0, top, im.size[0], bottom)
 area = imp.crop(box)
 area.show()
 areacp=area.copy()
 area=PreProcess(area)
 #area.show()
 left,right,top,bottom=trial2.MatchBox(area)
 box = (left, top-2, right, bottom-2)
 areacp = areacp.crop(box)
 areacp=Resize(areacp,400)
 #areacp.show()
 pix=areacp.load()
 for i in range(areacp.size[0]):
    for j in range(areacp.size[1]):
        if(pix[i,j]<110):
           areacp.putpixel((i,j),0)
        else:
           areacp.putpixel((i,j),255)

 areacp.show()
 #areacp= Cleanify(areacp)
 #areacp.show()
 return areacp
 
#########################################################################################

def NMode(im):
  imw= im.size[0]
  imh= im.size[1]
  pix=im.load()
  winw=1
  winh=1
  x=0 
  y=0
  while(x <= (imh-winh)):
    y=0
    while(y<= (imw-winw)):
         th=0
         for i in range(x,x+winh):
            for j in range(y,y+winw):
               th+= pix[j,i]
         th=th/(winw*winh)
         if th<80:       
          for i in range(x,x+winh):
            for j in range(y,y+winw):
                  im.putpixel((j,i),0)
               
         y+=winw
    x+=winh
  return im

####################################################################################

def Cleanify(im):
  imw= im.size[0]
  imh= im.size[1]
  pix=im.load()
  winw=3
  winh=3
  x=0 
  y=0
  while(x <= (imh-winh)):
    #print x
    y=0
    while(y<= (imw-winw)):
         avg=0
         for i in range(x,x+winh):
            for j in range(y,y+winw):
               avg+= pix[j,i]
         avg=avg/(winw*winh)   
         if(avg<126):
           avg=0
         else:
           avg=255  
         for i in range(x,x+winh):
            for j in range(y,y+winw):
                  im.putpixel((j,i),avg)
               
         y+=winw
    x+=winh
  return im
####################################################################################


   
   
   
   
  
  



