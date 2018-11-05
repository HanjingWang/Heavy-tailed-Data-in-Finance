# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 02:49:39 2018

@author: hanji
"""

import plotly
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='hanjingwang', api_key='3bYf12UCH4thFMJs8PpD')
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def log_returns(x):
    # input a list 
    return [np.log(x[i+1]/x[i]) for i in range(len(x)-1)]

def histogram(filename):
    df_list = []
    name_list = []
    for csv in os.listdir(filename):

        df = pd.read_csv(os.getcwd()+'\\'+filename+'\\'+csv)
        df_list.append(df)
        name_list.append(csv)
    trace0 = go.Histogram(
    x=df_list[0]['Open'],
    xbins=dict(start=np.min(df_list[0]['Open']), size=5, end=np.max(df_list[0]['Open'])),
    name = name_list[0]     
                    )
    trace1 = go.Histogram(
            x=df_list[1]['Open'], 
            name = name_list[1]
            )
    trace2 = go.Histogram(
            x=df_list[2]['Open'], 
            name = name_list[2]
            )
    trace3 = go.Histogram(
            x=df_list[3]['Open'],
            name = name_list[3]
            )
    trace4 = go.Histogram(
            x=df_list[4]['Open'],
            name = name_list[4] )
    fig = tools.make_subplots(rows=3, cols=2)
    fig.append_trace(trace0, 1, 1)
    fig.append_trace(trace1, 1, 2)
    fig.append_trace(trace2, 2, 1)
    fig.append_trace(trace3, 2, 2)
    fig.append_trace(trace4, 3, 1)
    layout = dict(
    title = filename
)
    py.iplot(fig, layout = layout, filename=filename)


def scatterplot(filename):
    df_list = []
    name_list = []
    for csv in os.listdir(filename):

        df = pd.read_csv(os.getcwd()+'\\'+filename+'\\'+csv)
        df_list.append(df)
        name_list.append(csv)
    trace0 = go.Scatter(
            x=df_list[0]['Date'],
            y=df_list[0]['Open'],
            name = name_list[0]     
                    )
    trace1 = go.Scatter(
            x=df_list[1]['Date'],
            y=df_list[1]['Open'], 
            name = name_list[1]
            )
    trace2 = go.Scatter(
            x=df_list[2]['Date'],
            y=df_list[2]['Open'], 
            name = name_list[2]
            )
    trace3 = go.Scatter(
            x=df_list[3]['Date'],
            y=df_list[3]['Open'],
            name = name_list[3]
            )
    trace4 = go.Scatter(
            x=df_list[4]['Date'],
            y=df_list[4]['Open'],
            name = name_list[4] )
    fig = tools.make_subplots(rows=3, cols=2)
    fig.append_trace(trace0, 1, 1)
    fig.append_trace(trace1, 1, 2)
    fig.append_trace(trace2, 2, 1)
    fig.append_trace(trace3, 2, 2)
    fig.append_trace(trace4, 3, 1)
    layout = dict(
    title = filename)
    py.iplot(fig, layout = layout, filename=filename)

def intraday_histogram_boxplot(path_list):
    
    dataframe_list = []
    name_list = []
    
    for path in path_list:
        # 'C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_second'
        for data in os.listdir(path):
            dataframe_list.append(pd.read_csv(path+'\\'+data,encoding='utf8'))
            name_list.append(data)
        for i in range(len(dataframe_list)):
            fig, axs = plt.subplots(1,2)
            axs[0].hist(dataframe_list[i].ix[:,2],bins=20)
            axs[0].set_title(name_list[i])
            axs[1].boxplot(dataframe_list[i].ix[:,2])
            axs[1].set_title(name_list[i])
            plt.show()
            plt.savefig('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\output\\vitualization\\histogram\\'+name_list[i][0:-4]+'.png')
            plt.close()


def histogram_log_returns(filename):
    df_list = []
    name_list = []
    for csv in os.listdir(filename):

        df = pd.read_csv(os.getcwd()+'\\'+filename+'\\'+csv)
        df_list.append(df)
        name_list.append(csv)
    trace0 = go.Histogram(
    x=log_returns(df_list[0]['Open']),
    name = name_list[0],
    histnorm='probability'
                    )
    trace1 = go.Histogram(
            x=log_returns(df_list[1]['Open']), 
            name = name_list[1],
            histnorm='probability'
            )
    trace2 = go.Histogram(
            x=log_returns(df_list[2]['Open']), 
            name = name_list[2],
            histnorm='probability'
            )
    trace3 = go.Histogram(
            x=log_returns(df_list[3]['Open']),
            name = name_list[3],
            histnorm='probability'
            )
    trace4 = go.Histogram(
            x=log_returns(df_list[4]['Open']),
            histnorm='probability',
            name = name_list[4] )
    fig = tools.make_subplots(rows=3, cols=2)
    fig.append_trace(trace0, 1, 1)
    fig.append_trace(trace1, 1, 2)
    fig.append_trace(trace2, 2, 1)
    fig.append_trace(trace3, 2, 2)
    fig.append_trace(trace4, 3, 1)
    layout = dict(
    title = filename,
    
)
    for i in range(5):
        print(np.mean(log_returns(df_list[i]['Open'])))
        print(np.median(log_returns(df_list[i]['Open'])))
    py.iplot(fig, layout = layout, filename=filename)   
    
def intraday_histogram_log_returns(path_list):
    
    df_list = []
    name_list = []
    
    for path in path_list:
        # 'C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_second'
        for data in os.listdir(path):
            df_list.append(pd.read_csv(path+'\\'+data,encoding='utf8'))
            name_list.append(data)
    trace0 = go.Histogram(
    x=log_returns(list(df_list[0].ix[:,1])),
    name = name_list[0]     
                    )
    trace1 = go.Histogram(
            x=log_returns(list(df_list[1].ix[:,1])), 
            name = name_list[1]
            )
    trace2 = go.Histogram(
            x=log_returns(list(df_list[2].ix[:,1])), 
            name = name_list[2]
            )
    trace3 = go.Histogram(
            x=log_returns(list(df_list[3].ix[:,1])),
            name = name_list[3]
            )
    trace4 = go.Histogram(
            x=log_returns(list(df_list[4].ix[:,1])),
            name = name_list[4] )
    trace5 = go.Histogram(
            x=log_returns(list(df_list[5].ix[:,1])), 
            name = name_list[5]
            )
    trace6 = go.Histogram(
            x=log_returns(list(df_list[6].ix[:,1])),
            name = name_list[6]
            )
    trace7 = go.Histogram(
            x=log_returns(list(df_list[7].ix[:,1])),
            name = name_list[7] )    
    fig = tools.make_subplots(rows=4, cols=2)
    fig.append_trace(trace0, 1, 1)
    fig.append_trace(trace1, 1, 2)
    fig.append_trace(trace2, 2, 1)
    fig.append_trace(trace3, 2, 2)
    fig.append_trace(trace4, 3, 1)
    fig.append_trace(trace5, 3, 2)
    fig.append_trace(trace6, 4, 1)
    fig.append_trace(trace7, 4, 2)  
    layout = dict(
    title = 'Big_data_log_returns_histogram'
)
    py.iplot(fig, layout = layout, filename='Big_data_log_returns_histogram')

       

if __name__ == '__main__':    
    histogram('20_year_daily')
    
    intraday_histogram_log_returns(["C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\output\\Comparison_mean_median\\Comparison_perday"])
    histogram_log_returns('20_year_monthly')

    path_list= ["C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\output\\Comparison_mean_median\\Comparison_perday"]
    df_list = []
    name_list = []
    
    for path in path_list:
        # 'C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_second'
        for data in os.listdir(path):
            df_list.append(pd.read_csv(path+'\\'+data,encoding='utf8'))
            name_list.append(data)
    for i in range(8):
        df_list[i] = df_list[i][df_list[i]<1000000]
        df_list[i] = df_list[i][df_list[i]>-1000000]
    fig1, ax1 = plt.subplots(8,1,figsize=(8, 30))
    for i in range(8):
        ax1[i].hist(list(df_list[i].ix[:,1]), 50, density = True)
        ax1[i].set_title(name_list[i])
        ax1[i].add_line(mlines.Line2D([np.mean(df_list[i].ix[:,1]),np.mean(df_list[i].ix[:,1])],[-1, 10000000000000], color = 'red', label = 'mean'))
        ax1[i].add_line(mlines.Line2D([np.median(df_list[i].ix[:,1]),np.median(df_list[i].ix[:,1])],[-1, 1000000000000], color = 'y', label = 'median'))
        ax1[i].legend()
    

    
    plt.show()
    plt.close()











