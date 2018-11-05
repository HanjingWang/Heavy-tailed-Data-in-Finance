# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:46:33 2018

@author: hanji
"""
import numpy as np
import os
import pandas as pd
def log_returns(x):
    # input a list 
    return [np.log(x[i+1]/x[i]) for i in range(len(x)-1)]

def euclidean(x,y):
    return np.sqrt(sum([(x[i]-y[i])**2 for i in range(len(x))]))
    
def subgradient(x,y,epsilon):
    # x: the starting point; let's start by the centriod of the y
    # y: a set of points {y1,y2,..yk} from R^N
    # if the distance between x and yi is less than epsilon, set the distance to 0
    phi = []

    for i in range(np.shape(y)[1]):
        if euclidean(x,y[:,i])>=0.00001:
            phi_i = np.array([y[:,i][j]-x[j] for j in range(len(x))])/euclidean(x,y[:,i])
            phi.append(phi_i)
        else:
            phi.append(0)
        
    subgradient = sum(phi)/len(phi)
    
    return np.array(subgradient)

def backtracking_subgradient(x, y, epsilon, iterations=10, learning_rate=0.1):
    # x: the starting point; let's start by the centriod of the y
    # y: a set of points {y1,y2,..yk} from R^N
    # if the distance between x and yi is less than epsilon, set the distance to 0
    # iterations: how many iterations you want to do for the backtracking
    # learning_rate: the learning rate for each step
    point = x
    starting_point = x
    trajectory = [point]
    distance = []
    distance.append(0)
    for i in range(iterations):
        subgrad = subgradient(point,y,epsilon)
 
        point = point + learning_rate * subgrad
        # print(point)
        trajectory.append(point)
        distance.append(euclidean(point,starting_point))
        # print(euclidean(point,starting_point))
    return np.array(trajectory), np.array(distance)



if __name__ == '__main__':
    # perpare data for the geometric median computation
    # read the five stock data to get the date and the open prices
    # compute the log return for each stock
    # merge the five dataset into one dataset
    dataframe_list = []
    name_list = []
    path = "C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\data\\20_year_Monthly"
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
    
    # generate the input for the geometric median computation
    y = np.array(df.ix[:,[1,2,3,4,5]])
    x = np.array([np.mean(y[i,:]) for i in range(np.shape(y)[0]) ])
    epsilon = 0.000001
    
    # result
    # create a dataframe to compare
    
    subgradient_track, distance = backtracking_subgradient(x,y,epsilon, iterations =100,learning_rate = 0.2)
    df['mean'] = x
    df['subgradient_median'] = subgradient_track[-1]
    # print out the distance between the geometric median and the mean estimator
    # daily: 0.45448554827727283
    # weekly: 0.513930112845
    # monthly: 0.592488129766
    print(euclidean(subgradient_track[-1], x))
    
    df.to_csv('Monthly_subgradient_median.csv',index = False)
    
    
    
    
    
    
    