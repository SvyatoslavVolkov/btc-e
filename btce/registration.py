# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:23:59 2018

@author: volkoff
"""

from btce import public_api, trade_api
from time import sleep
import datetime
import csv

# API Keys
user_info = {}
user_info['api_key'] = 'TFHZYNIN-8Z18D9IL-V3MH6P5F-Z7RW0EEJ-O7ONS5JG'
user_info['api_secret'] = '6c6db3c30c746140aba002408edbf51b9c777cb55ee410156110897f2957b303'
user_info['nonce'] = 100

pairs = ['btc_usd', 'ltc_usd', 'eth_usd', 'zec_usd', 'bch_usd']

directory = 'D:\\wex_log'

papi = public_api()

time_interval = 5

while(1) :
    date = datetime.datetime.now()
    for pair in pairs:
        ticker = papi.ticker(pair)
        price_filename = pair + '_' + date.strftime("%Y_%m_%d_%H") + '.csv'
        if(ticker.keys().__contains__('error')):
            continue
        
        csvfile = open(directory + '\\' + price_filename, 'a', newline='')
        csvwriter = csv.writer(csvfile, delimiter=';')
        csvwriter.writerow(list(ticker[pair].values()))
        csvfile.close()
        
#        print(pair)
    sleep(time_interval)