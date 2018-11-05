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

figure(num=None, figsize=(8, 12), dpi=80, facecolor='w', edgecolor='k')

def mean_median(data,n):
    if n >=1:
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
sub_df = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\output\\subgradient\\Weekly_subgradient_median.csv')
geo_df = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\output\\geomeric_median\\Weekly_geometric_median.csv')


mean =list(sub_df['mean'])
sub = list(sub_df['subgradient_median'])
geo = list(geo_df['g_median'])
date = list(sub_df['Date'])
Date = [datetime.strptime(date[i],'%Y-%m-%d') for i in range(len(date))]



# geometic median and subgredient median
fig1, ax1 = plt.subplots(3,1,figsize=(8, 18))
ax1[0].hist(sub, 50)
ax1[0].set_title('Geometric median using Subgradient')
ax1[0].set_xlabel('value')
ax1[0].set_ylabel('Frenquency')
ax1[1].hist(geo, 50)
ax1[1].set_title('Geometric Median using Weiszfeld')
ax1[1].set_xlabel('value')
ax1[1].set_ylabel('Frenquency')
ax1[2].plot(sub,geo)
ax1[2].set_title('Comparison')
ax1[2].set_xlabel('Geometric median using Subgradient')
ax1[2].set_ylabel('Geometric Median using Weiszfeld')
plt.show()
plt.close()


# Comparison between mean estimator and geometric median
fig2, ax2= plt.subplots()
ax2.plot(Date, mean, label = 'mean estimator')
ax2.plot(Date, sub, label = 'geometric median')
ax2.legend()
fig2.autofmt_xdate()
ax2.set_title('Comparison between geometic median and mean estimator')
ax2.set_xlabel('date')
ax2.set_ylabel('value')
plt.legend()
plt.show()
plt.close()

# mean-median estimator in different scales
# use the log returns of the AAPL.csv open prices per day
# for each scale, obtain one point

df = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_minute\\IBM_adjusted.txt', header = None)
data = log_returns(list(df.ix[:,2]))

mean_median_scale = []
scale = list(range(1,1001))
for i in range(1,1001):
    print(i)
    temp = mean_median(data, i)
    mean_median_scale.append(temp)
    
fig3, ax3= plt.subplots()
ax3.plot(scale, mean_median_scale)
ax3.add_line(mlines.Line2D([-1, 10000000000000],[np.mean(data),np.mean(data)], color = 'red', label = 'mean'))
ax3.add_line(mlines.Line2D([-1, 10000000000000],[np.median(data),np.median(data)], color = 'y', label = 'median'))
ax3.legend()
ax3.set_title('Different Scales for Mean-of-Median Estimators')
ax3.set_xlabel('scale')
ax3.set_ylabel('mean-of-medians')


# compare mean-median with mean estimator
# seperate the IBM_adjusted.txt randomly to 100 parts
# for each part, compute the mean and the mean-of-medians
seperate_data = seperate_randomly(data,100) 

mean = []
MeanMedians=[]
number = list(range(1,101))

count = 0
for i in seperate_data:
    print(count)
    mean.append(np.mean(i))
    MeanMedians.append(mean_median(i,100))
    count +=1

fig4, ax4= plt.subplots()
ax4.plot(number, mean, marker = 'o', color = 'black',label = 'mean')
ax4.plot(number, MeanMedians, marker = 'o', color = 'red',label = 'mean-of-median')

ax4.set_title('Comparison for Mean and Mean-of-Median Estimators')
ax4.set_xlabel('number')
ax4.set_ylabel('value')









