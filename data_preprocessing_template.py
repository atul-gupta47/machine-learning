# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:11:04 2017

@author: Atul Gupta
"""

#importing lib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import dataset
dataset = pd.read_csv("Data.csv")

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

#missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) 
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])