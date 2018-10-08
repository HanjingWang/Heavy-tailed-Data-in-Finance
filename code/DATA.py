# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:59:15 2018

@author: hanji
"""

import requests
import pandas as pd

def intraday_datasample(symbol, interval):
    '''
    symbol: the name for the stock
    interval: 1min, 5min, 15min,60min
    '''
    Base_url = "https://www.alphavantage.co/query"
    Url_post = {
                'function': 'TIME_SERIES_INTRADAY',
                'symbol': symbol,
                'interval': interval,
                'apikey': 'KDMFO36WPT9E64GA',
                'datatype' : 'json'
                }
    
    response=requests.get(Base_url, Url_post)
    jsontxt = response.json()
    
    time = list(list(jsontxt.values())[1].keys())
    open_price = [list(i.values())[0] for i in list(list(jsontxt.values())[1].values())]
    high_price = [list(i.values())[1] for i in list(list(jsontxt.values())[1].values())]
    low_price = [list(i.values())[2] for i in list(list(jsontxt.values())[1].values())]
    close_price = [list(i.values())[3] for i in list(list(jsontxt.values())[1].values())]
    volume = [list(i.values())[4] for i in list(list(jsontxt.values())[1].values())]
    
    # create a dictionary
    dic = {'time':time, 'open_price':open_price, 'high_price': high_price, 'low_price':low_price, 'close_price':close_price, 'volume':volume}
    
    df = pd.DataFrame(dic)
    string = symbol +'_'+ interval+'_' + 'data_sample.csv'
    df.to_csv(string)
    

def bitcoin(time_start, time_end, period_id):
    api_key = ['B0357CB5-F06D-47FA-A6F2-A3364633533B','B0D94F7A-28BD-447C-B5A3-978DBC5AC130',
               '48673383-E887-4C54-84D0-31368C1C8FA7', '8B435C5B-6BC4-4F74-83A0-4D4B1C0B2462'
               ,'0EA638C8-8508-4C7D-B22C-D05FD50FC068','5048A8F5-EFC9-4834-B681-5D514C47E87A',
               'BD914C62-B992-404A-986C-A2D8C16F4379','29C83E3D-5598-48A9-B96C-E97DECCCF72B',
               '5D3AD3A3-00C0-45DE-99EC-221261327672']

    Base_url = "https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/history"
    
    # an example for the jsontxt text we get from the api about the prices for bitcoin
    jsontxt_example = [{'price_close': 6445.05,
               'price_high': 6445.05,
               'price_low': 6423.05,
               'price_open': 6434.48,
               'time_close': '2018-09-06T08:49:58.0000000Z',
               'time_open': '2018-09-06T08:40:03.0000000Z',
               'time_period_end': '2018-09-06T08:50:00.0000000Z',
               'time_period_start': '2018-09-06T08:40:00.0000000Z',
               'trades_count': 136,
               'volume_traded': 55.50919893}]
    jsontxt = jsontxt_example
    bitcoin_data = []
    count = 0
    api_key_count = 0
    while(jsontxt[-1]['time_period_end']!=time_end):
        try:
            headers = {'X-CoinAPI-Key' : api_key[api_key_count]}
            Url_post = {
                    'period_id': period_id,
                    'time_start': time_start,
                    'time_end': time_end
                    }
            response = requests.get(Base_url,Url_post, headers=headers)
            jsontxt = response.json()
            bitcoin_data = bitcoin_data + jsontxt
            time_start = jsontxt[-1]['time_period_end']
            count = count +1
            print(count)
            
        except:
            print('reach the limits, change the key')
            api_key_count = api_key_count +1
            jsontxt = jsontxt_example
    return bitcoin_data

def csv_bitcoin(bitcoin_data):
    '''
    generate .csv file for the bitcoin_data
    '''
    price_close = [ i['price_close'] for i in bitcoin_data]
    price_high = [ i['price_high'] for i in bitcoin_data]
    price_low = [ i['price_low'] for i in bitcoin_data]
    price_open = [ i['price_open'] for i in bitcoin_data]
    time_period_end = [ i['time_period_end'] for i in bitcoin_data]
    time_period_start = [ i['time_period_start'] for i in bitcoin_data]
    
    dic = {'price_close':price_close,'price_high':price_high,'price_low':price_low,
           'price_open':price_open,'time_period_end':time_period_end, 'time_period_start':time_period_start}
    df = pd.DataFrame(dic)
    df.to_csv('Bitcoin.csv')
    
if __name__ == '__main__':
    
    intraday_datasample('AAPL','60min')    
    bitcoin_data = bitcoin('2017-10-01T00:00:00.0000000Z','2018-10-01T00:00:00.0000000Z','10MIN')
    csv_bitcoin(bitcoin_data)


























