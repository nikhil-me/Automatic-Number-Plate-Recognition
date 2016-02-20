import csv


X=[]
Y=[]
with open('train.csv','r') as f1:
	traindatareader=csv.reader(f1,delimiter=',')
	for line in traindatareader:
		#line.split(',')
		print len(line)
		X.append(line[0:783])
		Y.append(line[-1])



"""def traindata(path):
	image=os.listdir(path)
	#print image
	X=[]
	Y=[]
	for img in image:
		im=Image.open(path+"/"+img)
		pix=im.load()
		imw=im.size[0]
		print 
		imh=im.size[1]
		temp=[]
		for i in range(1,imh):
			for j in range(1,imw):
				temp.append(pix[i,j])
		#print temp
		#print "agigiaigiiig"
		#print "sgishgishishg"
		Y.append(img[0])
		X.append(temp)"""
