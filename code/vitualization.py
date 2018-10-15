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

if __name__ == '__main__':    
    histogram('20_year_daily')




