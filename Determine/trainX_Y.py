from multiprocessing import Pool
from PIL import Image
import os
import os.path
import re
import numpy 
import csv
import test

def traindata(path,inp_file):
	image=os.listdir(path)
        
	#print image
	X=[]
	Y=[]
	for img in image:
               
                
		im=Image.open(path+"/"+img)
		#im=im.resize((10,10),Image.ANTIALIAS)
                imw=im.size[0]
		#print imw
		imh=im.size[1]
		#print imh
		pix=im.load()
                for i in range(imw):
                     for j in range(imh):
                             if pix[i,j]<=130:
                                 im.putpixel((i,j),0)
                             else:
                                 im.putpixel((i,j),255)
                
		im=im.resize((24,24),Image.ANTIALIAS)
		im.show()
		imw1=im.size[0]
		imh1=im.size[1]
		temp=[]
		for i in range(0,imw1):
			for j in range(0,imh1):
				temp.append(int(pix[i,j]))
		print len(temp)
		#print "agigiaigiiig"
		#print "sgishgishishg"
		Y.append(img[0])
		X.append(temp)


	#print X
        #print Y
	with open(inp_file,'w') as f:
		writer=csv.writer(f,delimiter=',')
		for i in range(0,len(X)):
			#print i
			#print X[i]
			data=X[i]
			temp=Y[i]
			data.append(temp)
			#print data
			#print 
			#print
			#print
			#data=data.append(Y[i])
			#print data
			writer.writerow(data)
			#writer.writerow(['\n'])

traindata("/home/amit/Documents/btp-master/digit_images/allinone",'train_digit_images.csv')		 		 

#call the test_clf classifier with the csv file as input this function stores the output in csv format with first column as the true value of character and second column as predicted value of that character.
#test.test_clf('_test_real_images.csv','result_images.csv')
