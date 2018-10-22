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
            plt.savefig('C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\output\\vitualization\\histogram\\'+name_list[i]+'.png')
            plt.close()
    

if __name__ == '__main__':    
    histogram('20_year_daily')
    
    intraday_histogram_boxplot(['C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_second','C:\\Users\\hanji\\Desktop\\Heavy tailed data in Finance\\data\\Big_intraday_data\\per_minute'])



