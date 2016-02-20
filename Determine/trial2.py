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
#from initial import Resize
#import initial
from skimage import feature



def run(i):
 src="EX/EX"+str(i)+".jpg"

 im = Image.open(src)
 im=Resize(im,600)
 im=im.convert('L')
 im=FindEdges(im)
 im.show()
 Y1,Y2,count=DetermineY(im)
 print count
 for i in range(1,count+1):
   #if (Y2[i]-Y1[i])>10 :
     print str(Y1[i])+" "+str(Y2[i])
     for j in range(Y1[i],Y2[i]):
       im=Whiten(im,j)
 im.show()


##########################################################################
def FindEdges(img):
 imw=img.size[0]
 imh=img.size[1]
 pix=img.load()
 for i in range(1,imh-1):
   for j in range(1,imw-1):
      val=pix[j,i]
      diff=max(abs(val-pix[j-1,i]),abs(val-pix[j+1,i]),abs(val-pix[j,i-1]),abs(val-pix[j,i+1]))
      img.putpixel((j,i),diff)
 #im=feature.canny(im, sigma=3)
 img=sobel(img)
 return img
##################################################################################
def DetermineY(img):
 imw=img.size[0]
 imh=img.size[1]
 pix=img.load()
 thd=150
 Y1= ndarray((imh,),int)
 Y2= ndarray((imh,),int)
 insideImg=0
 count1=0
 count2=0
 EdgCount = ndarray((imh,),int)
 for i in range(imh):
   EdgCount[i]=0
   for j in range(imw-1):
      if  abs(pix[j,i]-pix[j+1,i])>thd :
         EdgCount[i]+=1
   #print ("%d : %d"%(i,EdgCount[i]))
 return EdgCount
 '''  
   if EdgCount[i]>15:
             if  insideImg==0:
                 count1+=1
                 Y1[count1]=i
                 insideImg=1
             else :
                 count2+=1
                 Y2[count2]=i
                 insideImg=0
 count=min(count1,count2)
 return Y1,Y2,count
 '''    
##############################################################################################
def MatchBox(im):
  imw=im.size[0]
  imh=im.size[1]
  pix=im.load()
  boxw=130
  boxh=30
  WCount = ndarray((imw,),int)
  i=0
  size=0
  while(i<(imw-boxw)):
       WCount[size]=0
       for j in range (i,i+boxw):
           for k in range (min(imh,boxh)):
               if(pix[j,k]>160):
                   WCount[size]+=1
       size+=1
       i+=1 
  maxm=-1
  max_x=0
  for i in range(0,(size)):
       if(WCount[i]>maxm):
          maxm=WCount[i]
          max_x=i
       #print str(i)+" , "+str(i+boxw)+" ,  0 , "+str(boxh)+" : "+str(WCount[i])
  #print"####"
  #print max_x
  #print"####"
  return max_x+5,max_x+boxw,0,boxh
            
                    
###############################################################################################    
def Whiten(img,y):
  imw=img.size[0]
  for i in range(imw):
    img.putpixel((i,y),255)
  return img 
##############################################################################################
def Plot(arr):
 x=len(arr)
 xarr = ndarray((x,),int)
 for i in range(1,x):
   xarr[i]=i
 plt.plot(xarr,list(arr))
 plt.axis([0,x,0,max(arr)+10])
 plt.show()
