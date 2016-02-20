#This part is to extract the no plate region and return as the utput of function Proe
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
from sobel import sobel #self writtn module
import trial2
from regiongrow import Rgrow #self written module
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


################################################################################################################

def Resize(img , bw):
 wpercent = (bw/ float(img.size[0]))
 hsize = int((float(img.size[1]) * float(wpercent)))
 img = img.resize((bw, hsize), Image.ANTIALIAS)
 return img
#####################################################################################################################
#binarization of image using global thresholding
def GBinarization(im,th):
  imw= im.size[0]
  imh= im.size[1]
  print imw
  print imh
  hs=im.histogram()
  th=0
  pix=im.load()
  if th==-1:
   for i in range(len(hs)):
    th+=i*int(hs[i])
  th=th/(imw*imh)
 
  for i in range(imh):
    for j in range(imw):
        if pix[j,i]<th :
           im.putpixel((j,i),0)
  return im
################################################################################################################

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
####################################################################################################################


###########################################################################################################################
from matplotlib import pyplot as plt
def PreProcess(im):
   
   im=NMode(im)
   im1 = ndimage.grey_erosion(im, size=(10,10))
   
   scipy.misc.imsave("eroded.jpg",im1)
   im1= Image.open("eroded.jpg")
   im=ImageOps.equalize(im,0)
   im=ImageChops.difference(im1, im)
   #print ("image height %d and width %d\n"%(imh,imw))
 
   im=GBinarization(im,50)#binarize the image
   
   return im
###################################################################################################################
#Processing the image

import cv2
def RegionExt(i):

 src="EXE/EX2/P"+str(i)+".jpg"
 try:
   im = Image.open(src)
 except :
   im = Image.open("EXE/EX2/P5280023.jpg")
 
 im=Resize(im,400)
 im=im.convert('L') #converts image into grayscale
 imp=im.copy()
 #im.show()
 im=PreProcess(im)
 #im.show()
 stage0_res=im.copy()
 #determine the column with maximum heuristic features
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

 try:
   im,top,bottom=Rgrow(im,150,max_j) 
 except :
    print "recusion depth error at image"+str(i)
    exit()
 #im.show()
 
 box = (0, max(0,top-10), im.size[0], min(im.size[1],bottom+40))
 area = imp.crop(box)
 stage1_res=area.copy()
 #area.show()
 areacp=area.copy()
 #areacp.show()
 orig=area.copy()
 area=PreProcess(area)
 #area.show()
 left,top,right,bottom=trial2.MatchBox(area)
 box = (max(0,left-10), max(0,top-10), min(im.size[0],right+15), min(im.size[1],bottom+10))
 orig=orig.crop(box)
 areacp = areacp.crop(box)
 stage2_res=areacp.copy()
 orig=Resize(orig,400)
 areacp=Resize(areacp,400)
 #areacp.show()
 pix=areacp.load()
 #areacp.show()
 return areacp,stage0_res,stage1_res,stage2_res


#######################################################################################
def Filter(img):#calculates the maximum continuous white width for each row and then blackens the row which has it more han half of the image width
  imw=img.size[0]
  imh=img.size[1]
  pix=img.load()
  thw=0
  thb=0
  Whw=ndarray((imh,),int)
  Blw=ndarray((imh,),int)
  for  i in range(imh):
      thw=0
      Whw[i]=0
      for j in range(imw):
           if pix[j,i]==255:
                Whw[i]+=1
 

  #for i in range(imh):
    #print str(i)+" : "+str(Whw[i])+" , "+str(Blw[i])
       
  for i in range(imh):
      if  Whw[i]>imw-30:
           for j in range(imw):
              img.putpixel((j,i),0)  
  return img       
 
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
  dp=ndarray((imh+1,imw+1),int)
  #dp that stores no of white pixels from 0,0 to i,j
  rowc=ndarray((imw+1,),int)
  
 
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


   
   
   
   
  
  



