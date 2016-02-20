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


def test_clf(inp_file,out_file):

	X=[]
	Y=[]
	with open(inp_file,'r') as f1:
		traindatareader=csv.reader(f1,delimiter=',')
		for line in traindatareader:
			#line.split(',')
			#print line
			X.append(line[0:576])
			print line[576]
			Y.append(line[576])
	
	#print X
	#print Y
	X_train=np.array(X)
	Y_train=np.array(Y)
	X_train=X_train.astype(np.float)/255.0
	#print X_train
	clf=joblib.load('train_pickle_chars.pkl')
			
	prediction=clf.predict(X_train)
	
	print prediction
	correct=0
	total=0
	with open(out_file,'w') as f:
		testresultwriter=csv.writer(f,delimiter=',')
		for i in range(0,len(prediction)):
			temp=[]
			temp.append(Y_train[i])
			temp.append(prediction[i])
			total+=1
			if prediction[i]==Y_train[i]:
				temp.append(1)
				correct+=1
			else:
				temp.append(0)
			testresultwriter.writerow(temp)
	
	
	print correct
	print total
