# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 02:28:47 2018

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
from tqdm import tqdm
import math
figure(num=None, figsize=(8, 12), dpi=80, facecolor='w', edgecolor='k')

def mean_median(data,n):
    if n >=1:
        if len(data)>n:
            number_list = list(range(0,len(data),int(len(data)/n)))
            sort_list = number_list+[len(data)-1]
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
    return [np.log(x[i+1]/x[i]) for i in tqdm(range(len(x)-1))]

# Compare the mean error and the median error for different size of the data and differnent scales
# when we find the median of means, we seperate the data equally

# do it and save it    
df = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\20_year_daily\\AAPL.csv')
df1 = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_minute\\IBM_adjusted.txt',header = None)
df2 = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_minute\\IVE_bidask1min.txt',header = None)
df3 = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_minute\\OIH_adjusted.txt',header = None)
df4 = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_minute\\WDC_bidask1min.txt',header = None)
df5 = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_second\\WDC_tickbidask.txt',header = None)
df6 = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_second\IVE_tickbidask.txt',header = None)

data_12 = log_returns(df[:4096]['Open'])
data_19 = log_returns(df2[:2**19].ix[:,2])
data_21 = log_returns(df1[:2**21].ix[:,2])
data_22 = log_returns(df6[:2**22].ix[:,2])
data_25 = log_returns(df5[:2**25].ix[:,2])

data_19 = pd.Series(data_19)
data_19 = data_19[data_19<1000000]
data_19 = data_19[data_19>-1000000]

pd.Series(data_12).to_csv('2^12_data.csv',index = False)
pd.Series(data_19).to_csv('2^19_data.csv',index = False)
pd.Series(data_21).to_csv('2^21_data.csv',index = False)
pd.Series(data_22).to_csv('2^22_data.csv',index = False)
pd.Series(data_25).to_csv('2^25_data.csv',index = False)

# read it again
data_12 = pd.read_csv("C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\2^12_data.csv", header = None)
data_19 = pd.read_csv("C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\2^19_data.csv", header = None)
data_21 = pd.read_csv("C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\2^21_data.csv", header  = None)
data_22 = pd.read_csv("C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\2^22_data.csv", header = None)
data_25 = pd.read_csv("C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\2^25_data.csv", header = None)

data_12 = data_12.ix[:,0]
data_19 = data_19.ix[:,0]
data_21 = data_21.ix[:,0]
data_22 = data_22.ix[:,0]
data_25 = data_25.ix[:,0]


data_19 = data_19[data_19<1000000]
data_19 = data_19[data_19>-1000000]


data_21 = data_21[data_21<1000000]
data_21 = data_21[data_21>-1000000]

data_22 = data_22[data_22<1000000]
data_22 = data_22[data_22>-1000000]


data_25= data_25[data_25<1000000]
data_25 = data_25[data_25>-1000000]


# repeat the same processes 5 times for the different size of the data
#log_n_k1 = list(np.linspace(0, 0.9, 100))
#scale = [int(len(data_12)**i) for i in log_n_k1]
#
#median_error_12 = []
#for i in tqdm(scale):
#    temp = mean_median(data_12, i)
#    median_error_12.append(np.mean(temp)-np.median(data_12))

'''
2^19
'''
log_n_k2 = list(np.linspace(0, 0.7, 200))
scale = [int(len(data_19)**i) for i in log_n_k2]
#scale = pd.Series(scale).unique()
#log_n_k2 = [math.log(i,len(data_19)) for i in scale]

median_error_19 = []
for i in tqdm(scale):
    temp = mean_median(data_19, i)
    median_error_19.append(np.mean(temp)-np.median(data_19))

mean = np.mean(median_error_19)
sd = np.std(median_error_19)


log_n_k19 = []
error19 = []
for i in range(len(scale)):
    if (median_error_19[i] > mean - 2 * sd) and (median_error_19[i] < mean + 2 * sd):
        log_n_k19.append(log_n_k2[i])
        error19.append(median_error_19[i])



'''
2^21
'''
log_n_k3 = list(np.linspace(0, 0.7, 200))
scale = [int(len(data_19)**i) for i in log_n_k3]
#scale = pd.Series(scale).unique()
#log_n_k3 = [math.log(i,len(data_19)) for i in scale]

median_error_21 = []
for i in tqdm(scale):
    temp = mean_median(data_21, i)
    median_error_21.append(np.mean(temp)-np.median(data_21))

mean = np.mean(median_error_21)
sd = np.std(median_error_21)


log_n_k21 = []
error21 = []
for i in range(len(scale)):
    if (median_error_21[i] > mean - 2 * sd) and (median_error_21[i] < mean + 2 * sd):
        log_n_k21.append(log_n_k3[i])
        error21.append(median_error_21[i])


'''
2^22
'''
log_n_k4 = list(np.linspace(0, 0.7, 200))
scale = [int(len(data_22)**i) for i in log_n_k4]
#scale = pd.Series(scale).unique()
#log_n_k4 = [math.log(i,len(data_22)) for i in scale]

median_error_22 = []
for i in tqdm(scale):
    temp = mean_median(data_22, i)
    median_error_22.append(np.mean(temp)-np.median(data_22))

mean = np.mean(median_error_22)
sd = np.std(median_error_22)


log_n_k22 = []
error22 = []
for i in range(len(scale)):
    if (median_error_22[i] > mean - 2 * sd) and (median_error_22[i] < mean + 2 * sd):
        log_n_k22.append(log_n_k4[i])
        error22.append(median_error_22[i])


'''
2^25
'''
log_n_k5 = list(np.linspace(0, 0.7, 200))
scale = [int(len(data_25)**i) for i in log_n_k5]
#scale = pd.Series(scale).unique()
#log_n_k5= [math.log(i,len(data_25)) for i in scale]

median_error_25 = []
for i in tqdm(scale):
    temp = mean_median(data_25, i)
    median_error_25.append(np.mean(temp)-np.median(data_25))

mean = np.mean(median_error_25)
sd = np.std(median_error_25)


log_n_k25 = []
error25 = []
for i in range(len(scale)):
    if (median_error_25[i] > mean - 2 * sd) and (median_error_25[i] < mean + 2 * sd):
        log_n_k25.append(log_n_k5[i])
        error25.append(median_error_25[i])



#median_error_12 = np.abs(median_error_12)
median_error_19 = np.abs(median_error_19)
median_error_21 = np.abs(median_error_21)
median_error_22 = np.abs(median_error_22)
median_error_25 = np.abs(median_error_25)

fig6, ax6 = plt.subplots(figsize=(20, 15))
#ax6.plot(log_n_k, mean_error_12, color = 'blue', label = 'N=12 mean error', marker = '_')
#ax6.plot(log_n_k1, median_error_12, color = 'red', label = 'N=2^12')
ax6.plot(log_n_k19, error19, color = 'blue', label = 'N=2^19')
ax6.plot(log_n_k21, error21, color = 'red', label = 'N=2^21')
ax6.plot(log_n_k22, error22, color = 'black', label = 'N=2^22')
ax6.plot(log_n_k25, error25, color = 'green', label = 'N=2^25')
#ax6.plot(log_n_k3, median_error_21, color = 'black', label = 'N=2^21')
#ax6.plot(log_n_k4, median_error_22, color = 'green', label = 'N=2^22')
#ax6.plot(log_n_k5, median_error_25, color = 'yellow', label = 'N=2^25')

ax6.legend()
ax6.set_title('Error for Different Size of the Data and Differnent Scales')
ax6.set_xlabel('log_N^k')
ax6.set_ylabel('Median Error')
plt.savefig('a.pdf')
plt.show()
