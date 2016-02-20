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
  print "Finding candidate region for No plate"
  imw=im.size[0]
  imh=im.size[1]
  pix=im.load()
  boxw=130
  boxh=30
  Wcount ={}
  i=0
  size=0
  dp=ndarray((imh+1,imw+1),int)
  #dp that stores no of white pixels from 0,0 to i,j
  rowc=ndarray((imw+1,),int)
  for i in range(imh):
       rowc[0]=0
       for j in range(imw):
            if j==0:
              rowc[j]=(pix[j,i]>140)
            else :
              rowc[j]=rowc[j-1]+(pix[j,i]>140)

            if i==0:
              dp[i,j]=rowc[j]
            else:
              dp[i,j]=dp[i-1,j]+rowc[j]

  for i in range(imw-boxw):
     for j in range(imh-boxh):
                key=str(i)+" "+str(j)
                Wcount[key]=dp[j+boxh,i+boxw]
                if(j>0):
                   Wcount[key]-=dp[j-1,i+boxw]
                if(i>0):
                   Wcount[key]-=dp[j+boxh,i-1]
                if(i>0 and j>0):
                   Wcount[key]+=dp[j-1,i-1]
                
                  
   

  '''
   for i in range(imw-boxw):
     for j in range(imh-boxh):
          key=str(i)+" "+str(j)
          Wcount[key]=0
          for k in range(i,min(imw,i+boxw)):
             for l in range(j,min(imh,j+boxh)):
                if(pix[k,l]>140):
                    Wcount[key]+=1  
  '''              
  maxm=-1
  max_x=0
  max_y=0
  for key,value in Wcount.iteritems():
        if(value>maxm):
             maxm=value
             max_x,max_y=key.split()
  max_x=int(max_x)
  max_y=int(max_y)     
  
       #print str(i)+" , "+str(i+boxw)+" ,  0 , "+str(boxh)+" : "+str(WCount[i])
  #print"####"
  #print max_x
  #print"####"
  return max_x,max_y,max_x+boxw,max_y+boxh
            
                    
###############################################################################################    

##############################################################################################
def Plot(arr):
 x=len(arr)
 xarr = ndarray((x,),int)
 for i in range(1,x):
   xarr[i]=i
 plt.plot(xarr,list(arr))
 plt.axis([0,x,0,max(arr)+10])
 plt.show()
