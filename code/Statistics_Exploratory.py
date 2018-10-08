# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:15:51 2018

@author: hanji
"""
import pandas as pd
import numpy as np
import os
import random

def log_returns(x):
    # input a list 
    return [np.log(x[i+1]/x[i]) for i in range(len(x)-1)]

def statistical_output(price_name):
    # price_name : Open Close High Low
    f= open('statistic_results.txt','w')
    for filename in os.listdir(os.getcwd()):
        if filename != 'intraday_data_sample' and filename != 'statistic_results.txt' and filename != 'Statistics_Exploratory.py':
            name = []
            mean = []
            median = []
            log_return_mean = []
            log_return_median = []
            for csv in os.listdir(filename):
                
                df = pd.read_csv(os.getcwd()+'\\'+filename+'\\'+csv)
                name.append(csv)
                mean.append(np.mean(df[price_name]))
                median.append(np.median(df[price_name]))
                log_return_mean.append(np.mean(log_returns(list(df[price_name]))))
                log_return_median.append(np.median(log_returns(list(df[price_name]))))
                
            dic={'name':name,'mean':mean,'median':median, 'log_return_mean':log_return_mean, 'log_return_median':log_return_median}
            df = pd.DataFrame(dic)
            f.write('===============================================\n')
            f.write('For '+filename)
            f.write('\n\n')
            f.write(str(df))
            f.write('\n\n')
    f.close()
    
def mean_median(data):
    number_list = list(random.sample(range(1, len(data)-1), 19))
    sort_list = number_list+[0,len(data)-1]
    sort_list.sort()
    mean_list = [np.mean(data[sort_list[i]:sort_list[i+1]]) for i in range(20)]
    return np.median(mean_list)
    
statistical_output('Open')    

def bitcoin_output():
    df = pd.read_csv('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\intraday_data_sample\\Bitcoin.csv')
    np.mean(df['price_open'])
    np.median(df['price_open'])
    np.mean(log_returns(df['price_open']))
    np.median(log_returns(df['price_open']))
    
    
    start_day = [x[0:10] for x in df['time_period_start']]
    df['start_day'] = pd.Series(start_day)
    unique_day = df['start_day'].unique()
    mean = []
    median = []
    log_return_mean = []
    log_return_median = []
    mean_median_list = []
    log_return_mean_median = []    
    groups = df.groupby('start_day')
    
    for day in unique_day:
        mean.append(np.mean(groups.get_group(day)['price_open']))
        median.append(np.median(groups.get_group(day)['price_open']))
        log_return_mean.append(np.mean(log_returns(list(groups.get_group(day)['price_open']))))
        log_return_median.append(np.median(log_returns(list(groups.get_group(day)['price_open']))))
        mean_median_list.append(mean_median(groups.get_group(day)['price_open']))
        log_return_mean_median.append(mean_median(log_returns(list(groups.get_group(day)['price_open']))))
    dic={'day':unique_day,'mean':mean,'median':median, 'log_return_mean':log_return_mean, 'log_return_median':log_return_median
         , 'mean_median':mean_median_list,'log_return_mean_median':log_return_mean_median}
    df = pd.DataFrame(dic)
    df.to_csv('bitcoin_output.csv')








