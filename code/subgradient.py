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
            phi_i = np.array([y[i,:][j]-x[j] for j in range(len(x))])/euclidean(x,y[i,:])
            phi.append(phi_i)
        else:
            phi.append(0)
        
    subgradient = sum(phi)/len(phi)
    
    return np.array(subgradient)

def subgradient_decent(x, y, epsilon, iterations=10, learning_rate=0.1):
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
    df['Year'] = [i[0:4] for i in list(df['Date'])]
    year = df['Year'].unique()
    groups = df.groupby('Year')
    df = df.drop(df.index[0])
    
    mean = []
    geometric_median_list = []
    median = []
    for i in year:
        temp = groups.get_group(i)
        
        # generate the input for the geometric median computation
        y = np.array(temp.ix[:,[1,2,3,4,5]])
        x = np.mean(temp, axis = 0)
        
        epsilon = 0.000001
        max_iteration = 100000
        g_median, distance = subgradient_decent(x,y,epsilon, iterations =100,learning_rate = 0.2)
        mean.append(x)
        median.append(np.median(temp, axis = 0))
        geometric_median_list.append(g_median[-1])
    
    # result
    # create a dataframe to compare
    
    for i in range(5):
        temp_mean = [j[i] for j in mean]
        temp_g_median = [j[i] for j in geometric_median_list]
        temp_median = [j[i] for j in median]
        name = name_list[i]
        df_temp = pd.DataFrame({'Year':year, 'mean':temp_mean,'g_median':temp_g_median,'median':temp_median})
        df_temp.to_csv('Geometric_median_yearly_'+name, index = False)
    
    
    
    
    