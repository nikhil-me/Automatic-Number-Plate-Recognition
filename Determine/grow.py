import numpy as np
def RegionGrow(img,X,Y,cost):
   imw= img.size[0]
   imh= img.size[1]
   pix=img.load()
   val=pix[X,Y]
   mat=np.zeros((imw,imh))
   img.putpixel((X,Y),255)
   mat[X][Y]=1
   th=150
   x1=X
   y1=Y-1
   x2=X+1
   y2=Y-1
   x3=X+1
   y3=Y
   x4=X+1
   y4=Y+1
   x5=X
   y5=Y+1
   x6=X-1
   y6=Y+1
   x7=X-1
   y7=Y
   x8=X-1
   y8=Y+1
   img,mat,cost=expand(x1,y1,val,img,mat,cost)
   img,mat,cpst=expand(x2,y2,val,img,mat,cost)
   img,mat,cost=expand(x3,y3,val,img,mat,cost)
   img,mat,cost=expand(x4,y4,val,img,mat,cost)
   img,mat,cost=expand(x5,y5,val,img,mat,cost)
   img,mat,cost=expand(x6,y6,val,img,mat,cost)
   img,mat,cost=expand(x7,y7,val,img,mat,cost)
   img,mat,cost=expand(x8,y8,val,img,mat,cost)
   return img




def expand(x1,y1,val,img,mat,cost):
   imw= img.size[0]
   imh= img.size[1]
   pix=img.load()
   th=150
   if  cost<th and x1>=0 and x1<imw and y1>=0  and y1<imh :
     if (mat[x1][y1]==0 and abs(val-pix[x1,y1])+cost< th):
             mat[x1][y1]=1
             cost+=abs(val-pix[x1,y1])
             RegionGrow(img,x1,y1,cost)
     else :
           if (mat[x1][y1]==0 and abs(val-pix[x1,y1])+cost>th) :
             img.putpixel((x1,y1),0)
             #RegionGrow(img,x1,y1,cost)
   else:
           if (cost>th and x1>=0 and x1<=imw and y1>=0  and y1<=imh) : 
             img.putpixel((x1,y1),0)
     
   return img,mat,cost
      
    

