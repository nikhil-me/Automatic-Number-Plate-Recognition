#install following
#sudo apt-get install gtk2-engines-pixbuf
#sudo apt-get install python-opencv
#sudo apt-get install python-PIL

import initial
import trial2
from PIL import Image
from numpy import ndarray
import os
import cv2
import numpy as np
import ImageFilter
from  Determine import regno
#from hlpr import hlpr

imw=0
imh=0
######################################################################################
#connected components segementation
lf=1000
rt=-1
up=1000
dn=-1
def find_char(x,y,pix,col,im):
   global lf
   lf=1000
   global rt
   rt=-1
   global up
   up=1000
   global dn
   dn=-1
   findchar(x,y,pix,col)
  
   box = (max(0,lf-4),max(0, up-5), min(imw,rt+4), min(imh,dn+5))
   imnw=im.crop(box)
   if imw*0.1 > rt-lf >8 and  imh*0.9>dn-up>20:
     #imnw.show()
     return imnw
   else  :
     return -1

def findchar(x,y,pix,col):
     col[x,y]=1
     global lf
     lf=min(x,lf)
     global up
     up=min(up,y)
     global rt
     rt=max(rt,x)
     global dn
     dn=max(dn,y)
     if(x>0 and col[x-1,y]==0 and pix[x-1,y]==0):
         findchar(x-1,y,pix,col)
     if(y>0 and col[x,y-1]==0 and pix[x,y-1]==0):
         findchar(x,y-1,pix,col)
     if(x<imw-1 and col[x+1,y]==0 and pix[x+1,y]==0):
         findchar(x+1,y,pix,col)
     if(y<imh-1 and col[x,y+1]==0 and pix[x,y+1]==0):
         findchar(x,y+1,pix,col)


def CleanImg(im):
  #cleaning the region around the boundry regions using properties of the characters and Integrs
  imw=im.size[0]
  imh=im.size[1]
  max_wh=ndarray((imw,),int)
  max_h=0
  bpx=ndarray((imw,),int)
  pix=im.load()
  for k in range(imw):
     max_wh[k]=0
     this_h=0
     bpx[k]=0
     for j in range(imh):
          if(pix[k,j]==0):
             max_wh[k]=max(max_wh[k],this_h) 
             this_h=0
          else:
             bpx[k]+=1
             this_h+=1
             
     max_wh[k]=max(max_wh[k],this_h) 
     max_h=max(max_h,max_wh[k])
     
  print im.size[1]
  for k in range(imw):
     if(abs(max_wh[k]-max_h)<10 or bpx[k]>imh*0.8):
         for j in range(imh):
               im.putpixel((k,j),255)  
  
  bpc=0
  #print "----"
  for k in range(imh):
       bpc=0
       for j in range(imw):
               if pix[j,k]==0:
                  bpc+=1
       #only for upper strip and lower strip
       if (bpc > imw*0.50 and  ( k < imh * 0.2  or k>imh*.6)) or k==0 or k==imh-1 :
           for j in range(imw):
               im.putpixel((j,k),255)
  return im
     
###################################################### MAIN CALLING FUNCTION#################################################
for i in range(5280116,5280126):
  im,st0_res,st1_res,st2_res=initial.RegionExt(i)
 
  global imw
  imw=im.size[0]
  global imh
  imh=im.size[1]
  pix=im.load()

  #simple binarization
  th=0
  for k in range(imw):
     for j in range(imh):
          th+=pix[k,j]
  th/=(imw*imh)
  th=th*1.2
  for k in range(imw):
     for j in range(imh):
         if pix[k,j]<th:
            im.putpixel((k,j),0)
         else:
            im.putpixel((k,j),255)
  
  
  im=CleanImg(im)  
  st3_res=im.copy()    
  #segmentation part
  imnew=im.copy()
  col=ndarray((imw,imh),int)
  for j in range(imw):
      for m in range(imh):
          col[j,m]=0
          imnew.putpixel((j,m),255)
  
  m=imh/2-5
  imlist=[]
  for j in range(imw):
       if pix[j,m]==0 and col[j,m]==0 :
              try:
               imlist.append(find_char(j,m,pix,col,im))
              except :
                   print "recusion depth error at image"+str(i)
                   exit()
              
  
 
 
  #return st0_res,st1_res,st2_res,st3_res,imlist
  
  print  "image no {0}".format(i)
  count={}
  j=0
 
       
  for pic in imlist:
       #pic=CleanImg(pic)
       try:
           pic.show()
           print "Enter Character in pic"
           inp=raw_input()
           inp=str(inp)
           if inp not in count.keys():
                count[inp]=0
           dest="DataSet/"+str(inp)+"/"
           with open('ct.txt','w') as fl:
            fl.write(str(i))
           fl.close()
           if not os.path.exists(dest):
              os.makedirs(dest)
           count[inp]=len(os.listdir(str(dest+'.')))+1
           dest+=str(count[inp])+".jpg"
           pic.save(dest)
           print "inserted image at {0} ,count :{1}".format(inp,count[inp])
       except:
        continue
       #print regno.getchar(pic),
       j+=1
  print ""
  








