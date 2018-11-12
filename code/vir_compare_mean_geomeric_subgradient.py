# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:57:44 2018

@author: hanji
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.pyplot import figure
import numpy as np
import random
import matplotlib.lines as mlines
import os

figure(num=None, figsize=(8, 12), dpi=80, facecolor='w', edgecolor='k')

def mean_median(data,n):
    if n >=1:
        if len(data)>n:
            number_list = list(random.sample(range(1, len(data)-1), n-1))
            sort_list = number_list+[0,len(data)-1]
            sort_list.sort()
            mean_list = [np.mean(data[sort_list[i]:sort_list[i+1]]) for i in range(n-1)]
            mean_list.append(np.mean(data[sort_list[-2]:sort_list[-1]+1])) # add the last one
            return np.median(mean_list)
    else:
        print('Error, please make sure n>=1')
        
def seperate_randomly(data,n):
    if n >=1:
        if len(data)>n:
            number_list = list(random.sample(range(1, len(data)-1), n-1))
            sort_list = number_list+[0,len(data)-1]
            sort_list.sort()
            result= [data[sort_list[i]:sort_list[i+1]] for i in range(n-1)]
            result.append(data[sort_list[-2]:sort_list[-1]+1])
            return result
    else:
        print('Error, please make sure n>=1')

def log_returns(x):
    # input a list 
    return [np.log(x[i+1]/x[i]) for i in range(len(x)-1)]

# perpare data
dataframe_list = []
name_list = []
path = "C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\output\\geomeric_median"
for data in os.listdir(path):
    dataframe_list.append(pd.read_csv(path+'\\'+data,encoding='utf8'))
    name_list.append(data[24:])


# Comparison between mean estimator and geometric median
fig2, ax2= plt.subplots(5,1,figsize=(8, 26))

for i in range(5):
    Date = [datetime.strptime(str(dataframe_list[i]['Year'][j]),'%Y') for j in range(len(dataframe_list[i]['Year']))]
    ax2[i].plot(Date, dataframe_list[i]['mean'], label = 'mean estimator',marker = 'o')
    ax2[i].plot(Date, dataframe_list[i]['g_median'], label = 'geometric median estimator',marker = 'o')
    ax2[i].plot(Date, dataframe_list[i]['median'], label = 'median estimator',marker = 'o')
    ax2[i].set_title(name_list[i])
    ax2[i].legend()


plt.show()
plt.close()

# mean-median estimator in different scales
# use the log returns of the AAPL.csv open prices per day
# for each scale, obtain one point

df = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\20_year_daily\\AAPL.csv')
data = log_returns(list(df['Open']))

quantile50 = []
quantile10 = []
quantile90 = []
mean = np.repeat(np.mean(data),100)
median = np.repeat(np.median(data),100)

scale = list(range(1,101))
for i in range(1,101):
    temp = []
    print(i)
    for j in range(1000):

        temp.append(mean_median(data, i))
    quantile50.append(np.quantile(temp, 0.5))
    quantile10.append(np.quantile(temp, 0.1))
    quantile90.append(np.quantile(temp, 0.9))
    
    
fig3, ax3= plt.subplots()
ax3.plot(scale, quantile50, color = 'red', label = '50% quantile')
ax3.plot(scale, quantile10, color = 'y', label = '10% quantile')
ax3.plot(scale, quantile90, color = 'b', label = '90% quantile')
ax3.plot(scale, mean, color = 'black', label = 'mean')
ax3.plot(scale, median, color = 'green', label = 'median')
ax3.legend(fontsize = 'small')
ax3.set_title('Different Scales for Median-of-means Estimators')
ax3.set_xlabel('scale')
ax3.set_ylabel('median-of-means')


# compare mean-median with mean estimator
# seperate the AAPL.csv randomly to 20 parts
# for each part, compute the mean and the median-of-means

df = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_minute\\IBM_adjusted.txt',header = None)
data = pd.Series(log_returns(list(df.ix[:,2])))
data= data[data<1000000]
data= data[data>-1000000]
seperate_data = seperate_randomly(data,100) 

mean = []
MeanMedians=[]
number = list(range(1,101))
difference = []
count = 0
for i in seperate_data:
    if len(i)>100:
        print(count)
        mean.append(np.mean(i))
        MeanMedians.append(mean_median(i,100))
        difference.append(np.mean(i) - mean_median(i,100))
        count +=1

fig4, ax4= plt.subplots()
ax4.hist(difference, bins = 50)
ax4.legend()
ax4.set_title('Difference for Mean and Median-of-means Estimators')


fig5, ax5= plt.subplots(2,1,figsize=(8, 12))
ax5[0].plot(range(len(mean)), list(np.array(mean)[np.argsort(difference)]), color = 'red', label = 'sample mean', marker = 'o')
ax5[0].plot(range(len(mean)), list(np.array(MeanMedians)[np.argsort(difference)]), color = 'blue', label = 'sample mean', marker = 'o')
plt.show()







