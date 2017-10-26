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