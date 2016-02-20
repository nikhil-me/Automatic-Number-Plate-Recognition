from multiprocessing import Pool
from PIL import Image
import os
import os.path
import re
import numpy as np
import csv
import sklearn
from sklearn.externals import joblib
import pickle
from sklearn import svm
from sklearn.svm import SVC

def getchar(im):
	clf_char=joblib.load('train_pickle_chars.pkl')
	#im=Image.open(filename)
	imw=im.size[0]
	imh=im.size[1]
	pix=im.load()
	for i in range(imw):
		for j in range(imh):
			if pix[i,j]<=130:
				im.putpixel((i,j),0)
			else:
				im.putpixel((i,j),255)
	im=im.resize((24,24),Image.ANTIALIAS)
	imw=im.size[0]
	imh=im.size[1]
	temp=[]
	for i in range(imw):
		for j in range(imh):
			temp.append(int(pix[i,j]))
	print len(temp)
	X=[]
	X.append(temp)
	X_test=np.array(X)
	X_test=X_test.astype(np.float)/255.0
	prediction=clf_char.predict(X_test)
	print prediction
	return prediction

def getdigit(im):
	clf_char=joblib.load('train_pickle_digits.pkl')
	#im=Image.open(filename)
	imw=im.size[0]
	imh=im.size[1]
	pix=im.load()
	for i in range(imw):
		for j in range(imh):
			if pix[i,j]<=130:
				im.putpixel((i,j),0)
			else:
				im.putpixel((i,j),255)
	im=im.resize((24,24),Image.ANTIALIAS)
	imw=im.size[0]
	imh=im.size[1]
	temp=[]
	for i in range(imw):
		for j in range(imh):
			temp.append(int(pix[i,j]))
	print len(temp)
	X=[]
	X.append(temp)
	X_test=np.array(X)
	X_test=X_test.astype(np.float)/255.0
	prediction=clf_char.predict(X_test)
	print prediction
	return prediction
'''
getchar(Image.open('3.JPG'))
getdigit(Image.open('0.JPG'))
getdigit(Image.open('1.JPG'))
'''
