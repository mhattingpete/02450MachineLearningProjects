'''
Paths --
Toolbox path: ../02450 - Machine Learning/Toolbox/
Data path: ./insuranceCompany_Data/
    {'ticdata2000.txt', 'ticeval2000.txt', 'tictgts2000.txt'}
'''
import os
import sys
import numpy as np

# Add path to course toolbox
abs_path = os.path.dirname(os.path.abspath(__file__))
par_path = os.path.dirname(abs_path)
par_par_path = os.path.dirname(par_path)
sys.path.append(par_par_path + '/02450 - Machine Learning/Toolbox/02450Toolbox_Python/Scripts')
sys.path.append(par_par_path + '/02450 - Machine Learning/Toolbox/02450Toolbox_Python/Tools')

# Check if data set exists
datafile = ['ticdata2000.txt', 'ticeval2000.txt', 'tictgts2000.txt']
for fname in datafile:
    if not os.path.isfile(par_path + '/insuranceCompany_Data/' + fname):
        print(fname+' is missing!', file=sys.stderr)
sys.stderr.flush()

# Load data from matlab file
X = np.loadtxt(par_path + '/insuranceCompany_Data/ticdata2000.txt')
y = X[:,-1]
X = X[:, 0:-1]

X_eval = np.loadtxt(par_path + '/insuranceCompany_Data/ticeval2000.txt')
y_eval = np.loadtxt(par_path + '/insuranceCompany_Data/tictgts2000.txt')

N = X.shape[0]
M = X.shape[1]
N_eval = X_eval.shape[0]
