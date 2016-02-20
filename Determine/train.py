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

X=[]
Y=[]
with open('train_images_chars.csv','r') as f1:
	traindatareader=csv.reader(f1,delimiter=',')
	for line in traindatareader:
		#line.split(',')
		#print line
		X.append(line[0:576])
		print line[576]
		Y.append(line[576])

print X
print Y
X_train=np.array(X)
Y_train=np.array(Y)
X_train=X_train.astype(np.float)/255.0
print X_train
clf=svm.SVC()
clf.fit(X_train,Y_train)

joblib.dump(clf,'train_pickle_chars.pkl')
		



