# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 23:53:34 2018

@author: hanji
"""

import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import cdist
import pandas as pd
import os


def geometic_median(x,y,epsilon,max_iteration):
    # x: the starting point; let's start by the centriod of the y
    # y: a set of points {y1,y2,..yk} from R^N
    # epsilon: apply Weiszfeld's algorithm until the distance between steps is less than epsilon.
    # max_iteration: the maximum iteration
    iteration = 1
    track = []
    track.append(x)
    while iteration <= max_iteration:
        print(iteration)
        w = [1/distance.euclidean(x,y[i,:]) for i in range(np.shape(y)[0]) ]
        x_new = sum([w[i]*y[i,:] for i in range(np.shape(y)[0])])/sum(w)
        track.append(x_new)
        if distance.euclidean(x,x_new)<epsilon:
            
            return x_new, iteration, track
            break
            
        else:
            x=x_new
            iteration = iteration+1
    else:
        return x, iteration, track

def log_returns(x):
    # input a list 
    return [np.log(x[i+1]/x[i]) for i in range(len(x)-1)]

def weiszfeld_method(y,epsilon, max_iteration):
    """
    Weiszfeld's algorithm as described on Wikipedia.
    """

    def distance_func(x):
        return cdist([x], y)

    # initial guess: centroid
    guess = y.mean(axis=0)

    iters = 0

    while iters < max_iteration:
        distances = distance_func(guess).T
        print(distances)
        print('old')
        # catch divide by zero
        # TODO: Wikipedia cites how to deal with distance 0
        distances = np.where(distances == 0, 1, distances)
        print(distances)
        guess_next = (y/distances).sum(axis=0) / (1./distances).sum(axis=0)

        guess_movement = np.sqrt(((guess - guess_next)**2).sum())

        guess = guess_next

        if guess_movement <= epsilon:
            break

        iters += 1

    return guess

dataframe_list = []
name_list = []
path = "C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\data\\20_year_daily"
for data in os.listdir(path):
    dataframe_list.append(pd.read_csv(path+'\\'+data,encoding='utf8'))
    name_list.append(data)
for i in range(len(name_list)):
    dataframe_list[i] = dataframe_list[i][['Date','Open']]
    dataframe_list[i].columns = ['Date',name_list[i]+'log_returns']
    
df = pd.merge(dataframe_list[0],dataframe_list[1])
for i in range(3):
    df = pd.merge(df,dataframe_list[2+i])
        
for i in range(len(df.columns)-1):
    df.ix[1:,1+i] = log_returns(df.ix[:,1+i])
df = df.drop(df.index[0])
y = np.array(df.ix[:,[1,2,3,4,5]])
x = list(np.mean(y, axis = 0))
geo_median, iterations, track = geometic_median(x, y, 0.0000001, 500)


# check
import  numpy.random as rd

A = rd.randn(5,5)


Q,R = np.linalg.qr(A)

data_rot = y@Q
#x = list(np.mean(data_rot, axis = 0))
geo_median_rot, iteration1, track1 = geometic_median(x,data_rot, 0.0000001, 500)

Q@geo_median_rot == geo_median













