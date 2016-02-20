from multiprocessing import Pool
from PIL import Image
import os
import os.path
import re



#p=Pool(5)

def process_fpath(path,inc):
    listing=os.listdir(path)
    #print listing
    for image in listing:
       #print image
       label=image.split('_')[-2]
       pattern=r'[0-9|a-z]'
       if re.match(pattern,label) or (".MIS" in image) or (".CLS" in image):
           continue
       im=Image.open(path+"/"+image)
       im=im.convert('L')
       imw=im.size[0]
       imh=im.size[1]
       pix=im.load()
       start=0
       flag=0
       end=28
       flag1=0
       flag2=0
       flag3=0
       left=28
       right=0
       
       for i in range(1,imh):
          for j in range(1,imw):
             if (pix[i,j]!=255):
                flag=1
             if (flag==1):
                start=i
                break
          if (flag==1):
             break
       
       '''
       for i in range(imh-50,imh-49):
          for j in range(1,imw):
              print pix[i,j]
       '''
       for i in range(imh-1,-1,-1):
          for j in range(1,imw):
              if (pix[i,j]!=255):
                 flag1=1
              if (flag1==1):
                 end=i
                 break
          if(flag1==1):
             break
       
       for i in range(1,imh):
          flag2=0
          for j in range(1,imw):
              if (pix[i,j]!=255):
                 flag2=1
                 left=min(left,j)
                 break
                  
       for i in range(imh-1,-1,-1):
           flag3=0
           for j in range(imw-1,-1,-1):
              if (pix[i,j]!=255):
                 flag3=1
              if (flag3==1):
                 right=max(right,j)
                 break
       #print left 
       #print start
       #print right
       #print end
       box=(left-5,start-10,right+10,end+10)
       im=im.crop(box)
       #im.show()
       im=im.resize((10,10),Image.ANTIALIAS)
       #im.save()
       #im.show()
       im1=im.copy()
       im1=im1.resize((10,10),Image.ANTIALIAS)
       loc=os.path.join('/home/amit/Documents/btp-master/test_real_char_images',label+'_'+str(inc)+".jpg")
       im1.save(loc)
       inc=inc+1
    return inc
       #im.show()
       #print start
       #print inc
       #im.save(os.path.join(path2,path), "JPEG")
       
process_fpath("/home/amit/Documents/btp-master/TEST/chars")         
