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
    aapl_name = []
    aapl_mean = []
    aapl_median = []
    aapl_log_return_mean = []
    aapl_log_return_median = []
    for filename in os.listdir(os.getcwd()):
        if filename != 'intraday_data_sample' and filename != 'statistic_results.txt':
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
            aapl_name.append(filename)
            aapl_mean.append(mean[0])
            aapl_median.append(median[0])
            aapl_log_return_mean.append(log_return_mean[0])
            aapl_log_return_median.append(log_return_median[0])
            f.write('===============================================\n')
            f.write('For '+filename)
            f.write('\n\n')
            f.write(str(df))
            f.write('\n\n')
    dic1 = {'name':aapl_name,'mean':aapl_mean,'median':aapl_median, 'log_return_mean':aapl_log_return_mean, 'log_return_median':aapl_log_return_median}
    df1 = pd.DataFrame(dic1)
    f.write('===============================================\n')
    f.write('For AAPL Data')
    f.write('\n\n')
    f.write(str(df1))
    f.write('\n\n')
    f.close()
    
def mean_median(data,n):
    if n >1:
        number_list = list(random.sample(range(1, len(data)-1), n-1))
        sort_list = number_list+[0,len(data)-1]
        sort_list.sort()
        mean_list = [np.mean(data[sort_list[i]:sort_list[i+1]]) for i in range(n)]
        mean_list.append(np.mean(data[sort_list[-2]:sort_list[-1]+1])) # add the last one
        return np.median(mean_list)
    else:
        print('Error Please make sure n>=1')
    
def bitcoin_output(n):
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
        mean_median_list.append(mean_median(groups.get_group(day)['price_open'],n))
        log_return_mean_median.append(mean_median(log_returns(list(groups.get_group(day)['price_open'])),n))
    dic={'day':unique_day,'mean':mean,'median':median, 'log_return_mean':log_return_mean, 'log_return_median':log_return_median
         , 'mean_median':mean_median_list,'log_return_mean_median':log_return_mean_median}
    df = pd.DataFrame(dic)
    df.to_csv('bitcoin_output.csv')
    



def intraday_data(df,column,n):  
    unique_day = df['Date'].unique()
    mean = []
    median = []
    log_return_mean = []
    log_return_median = []
    mean_median_list = []
    log_return_mean_median = []    
    groups = df.groupby('Date')
    day1=[]
    for day in unique_day:
            temp = groups.get_group(day)[column]
            if len(temp)>n+1:
                print(day)
                day1.append(day)
                mean.append(np.mean(temp))
                median.append(np.median(temp))
                log_return_mean.append(np.mean(log_returns(list(temp))))
                log_return_median.append(np.median(log_returns(list(temp))))
                mean_median_list.append(mean_median(temp,n))
                log_return_mean_median.append(mean_median(log_returns(list(temp)),n))
    dic={'day':day1,'mean':mean,'median':median, 'log_return_mean':log_return_mean, 'log_return_median':log_return_median
         , 'mean_median':mean_median_list,'log_return_mean_median':log_return_mean_median}
    df_new = pd.DataFrame(dic)
    return df_new


def intraday_period(df,column,n,period):
    day = df['Date'].unique()
    temp = {}
    
    length = len(day)
    number = length//period
    
    part = list(np.repeat(np.array(range(1,number+1)),period))+[number+1 for i in range(length%period)]
    for i in range(len(day)):
        temp[list(day)[i]]=part[i]
    temp2 = [str(temp[i]) for i in df['Date']]
    df['Period_count']=temp2
    
    groups = df.groupby('Period_count')
    
    unique_period = df['Period_count'].unique()
    mean = []
    median = []
    log_return_mean = []
    log_return_median = []
    mean_median_list = []
    log_return_mean_median = []    
    period_name=[]

    
    for day in unique_period:
        temp = groups.get_group(day)[column]
        temp2 = list(groups.get_group(day)['Date'])
        if len(temp)>n+1:
            print(day)
            period_name.append(temp2[0]+'-'+temp2[-1])
            mean.append(np.mean(temp))
            median.append(np.median(temp))
            log_return_mean.append(np.mean(log_returns(list(temp))))
            log_return_median.append(np.median(log_returns(list(temp))))
            mean_median_list.append(mean_median(temp,n))
            log_return_mean_median.append(mean_median(log_returns(list(temp)),n))
    dic={'period':period_name,'mean':mean,'median':median, 'log_return_mean':log_return_mean, 'log_return_median':log_return_median
             , 'mean_median':mean_median_list,'log_return_mean_median':log_return_mean_median}
    df_new = pd.DataFrame(dic)
    return df_new        
        
if __name__ == '__main__':
    
    # statistical ananlysis for stock price per day, week and month
    statistical_output('Open')

    # compare the mean,median, and mean_median each day for intraday data
    df = pd.read_csv('OIH_adjusted.txt',header = None)
    df.columns = ['Date','Time','Open','High','Low','Close','Volume']
    df_new = intraday_data(df,'Open',20)
    df_new.to_csv('OIH_adjusted_mean_median_perday.csv',index=False)
    
    # Three day periods
    path_list = ['C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_second','C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_minute']
    dataframe_list = []
    name_list = []
    period=5
    for path in path_list:
        # 'C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_second'
        for data in os.listdir(path):
            dataframe_list.append(pd.read_csv(path+'\\'+data,encoding='utf8'))
            name_list.append(data)
    for i in range(len(name_list)):
        df = dataframe_list[i].ix[:,[0,2]]
        df.columns = ['Date','Open']
        df_new=intraday_period(df,'Open',20,period)
        df_new.to_csv(name_list[i]+'.csv', index=False)
        



