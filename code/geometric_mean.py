# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 01:07:41 2018

@author: hanji
"""

import numpy as np
from scipy.spatial import distance
import pandas as pd
import os


def geometic_median(x,y,epsilon,max_iteration):
    # x: the starting point; let's start by the centriod of the y
    # y: a set of points {y1,y2,..yk} from R^N
    # epsilon: apply Weiszfeld's algorithm until the distance between steps is less than epsilon.
    # max_iteration: the maximum iteration
    iteration = 1
    while iteration <= max_iteration:
        print(iteration)
        w = [1/distance.euclidean(x,y[i,:]) for i in range(np.shape(y)[1]) ]
        x_new = sum([w[i]*y[i,:] for i in range(np.shape(y)[1])])/sum(w)
        if distance.euclidean(x,x_new)<epsilon:
            
            return x_new, iteration
            break
            
        else:
            x=x_new
            iteration = iteration+1
    else:
        return x, iteration

def log_returns(x):
    # input a list 
    return [np.log(x[i+1]/x[i]) for i in range(len(x)-1)]
   
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
        g_median, iteration = geometic_median(x,y,epsilon,max_iteration)
        mean.append(x)
        median.append(np.median(temp, axis = 0))
        geometric_median_list.append(g_median)
    
    for i in range(5):
        temp_mean = [j[i] for j in mean]
        temp_g_median = [j[i] for j in geometric_median_list]
        temp_median = [j[i] for j in median]
        name = name_list[i]
        df_temp = pd.DataFrame({'Year':year, 'mean':temp_mean,'g_median':temp_g_median,'median':temp_median})
        df_temp.to_csv('Geometric_median_yearly_'+name, index = False)

    
















