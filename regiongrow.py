import numpy 
import sys

sys.setrecursionlimit(10000)

def Rgrow(im,a,b):
  imw= im.size[0]
  imh= im.size[1]
  pix=im.load()
  mat=numpy.zeros(shape=(imw,imh))
  D=numpy.zeros(shape=(imw,imh))
  dist=0
  im=grow(im,pix,mat,imw,imh,a,b,a,b,dist)
  start =-1
  end=-1
  for i in range(imw):
     for j in range(imh):
        #print mat[i,j],
        if(int(mat[i,j])==0):
         im.putpixel((i,j),0)
        else:
          if( start==-1):
                  start=j
     
        
     #print ' '
  j=imh-1
  flag=0
  
  
  while(j>start):
         count=0
         for i in range(imw):
            if(int(mat[i,j])==1):
               count=count+1 
         if(count>10):
           end=j
           break
         j=j-1
             
  #print "start ",start
  #print "end ",end
  #im.show()
  
  return im,start-5,end
  
            


def grow(im,pix,mat,imw,imh,sa,sb,a,b,dist):
   #print ((a,b),dist)
   pixdist=(sa-a)**2+(sb-b)**2
   pixdist=pixdist**0.5
   if(a>=0 and a<imw and b>=0 and b<imh and mat[a,b]==0 and dist<800 and pixdist<40):
        mat[a,b]=1
        if(a-1>=0 and a-1<imw and b>=0 and b<imh):
         im=grow(im,pix,mat,imw,imh,sa,sb,a-1,b,dist+abs(pix[a,b]-pix[a-1,b]));
        if(a+1>=0 and a+1<imw and b>=0 and b<imh):
         im=grow(im,pix,mat,imw,imh,sa,sb,a+1,b,dist+abs(pix[a,b]-pix[a+1,b]));
        if(a>=0 and a<imw and b-1>=0 and b-1<imh):
         im=grow(im,pix,mat,imw,imh,sa,sb,a,b-1,dist+abs(pix[a,b]-pix[a,b-1]));
        if(a>=0 and a<imw and b+1>=0 and b+1<imh):
         im=grow(im,pix,mat,imw,imh,sa,sb,a,b+1,dist+abs(pix[a,b]-pix[a,b+1]));
   return im;
        
        
  
