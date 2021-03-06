'''
LogisticRegression
- KFold cross validation for train error calculation
'''
import numpy as np
from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show, axhline, legend
import sklearn.linear_model as lm
from sklearn import cross_validation
from resolve_path import *

X_train2, X_test2, y_train2, y_test2 = cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)

# K-fold crossvalidation
K = 10
max_attributes = X_train2.shape[1]-1

CV = cross_validation.KFold(X_train2.shape[0],K,shuffle=True)
#errors = np.zeros((K,l1_max_nodes-1,l2_max_nodes))
errors = np.zeros((K,max_attributes))

k=0
for train_index, test_index in CV:
    print('Crossvalidation fold: {0}/{1}'.format(k+1,K))

    # extract training and test set for current CV fold
    X_train, y_train = X_train2[train_index,:], y_train2[train_index]
    X_test, y_test = X_train2[test_index,:], y_train2[test_index]

    for i in range(0,max_attributes):
    	mod = lm.LinearRegression()
    	mod = mod.fit(X_train[:,0:i+1], y_train)
    	y_est = mod.predict(X_test[:,0:i+1])
    	residuals = (y_est-y_test).astype(float)
    	errors[k,i] = np.dot(residuals,residuals)/y_test.shape[0]

    k+=1



# Plot the classification error rate
print('Error rate: ',100*np.mean(errors,0))
print('Idx of min value:',np.argmin(np.mean(errors,0)))
