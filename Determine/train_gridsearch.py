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
from sklearn import svm, datasets, cross_validation
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
"""scikit-learn classifiers and cross validation utils
 from sklearn.ensemble import RandomForestClassifier (A random forest is a meta estimator
 that fits a number of decision tree classifiers on various sub-samples of the dataset and use
 averaging to improve the predictive accuracy and control over-fitting.)"""
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV #for cross validation




X=[]
Y=[]
with open('train_digit_images.csv','r') as f1:
	traindatareader=csv.reader(f1,delimiter=',')
	for line in traindatareader:
		#line.split(',')
		#print line
		X.append(line[0:576])
		print line[576]
		Y.append(line[576])

print X
print Y
X_float=np.array(X)
Y_float=np.array(Y)
X_float=X_float.astype(np.float)/255.0


X_train, X_test, Y_train, Y_test = train_test_split(
    X_float, Y_float, test_size=0.10, random_state=0)

# Set the parameters by cross-validation
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [0.125,0.1,0.128,0.20,0.001,0.01,0.0001,0.00001,0.000001],
                     'C': [1,10,0.98,100,1000,10000,0.1,100000,1000000,10000000]}]
#,{'kernel': ['linear'], 'C': [1,1.05,100,1000,0.01,1.5,0.05,10]}

scores = ['precision']
print (scores)

for score in scores:
    print "# Tuning hyper-parameters for %s" % score 
    print

    clf = GridSearchCV(svm.SVC(C=1), tuned_parameters, cv=5, scoring=score)
    clf.fit(X_train, Y_train)

    print "Best parameters set found on development set:"
    print
    print clf.best_estimator_
    print
    print "Grid scores on development set:"
    print
    for params, mean_score, scores in clf.grid_scores_:
        print "%0.3f (+/-%0.03f) for %r"% (mean_score, scores.std() / 2, params) 
    print

    print "Detailed classification report:"
    print
    print "The model is trained on the full development set."
    print "The scores are computed on the full evaluation set."
    print
    Y_true, Y_pred = Y_test, clf.predict(X_test)
    print classification_report(Y_true, Y_pred)
    print





joblib.dump(clf,'train_pickle_digits.pkl')
		



