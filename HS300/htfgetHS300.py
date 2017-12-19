# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:26:33 2017

@author: Alpha
"""
'''
函数功能说明：
利用wind获取沪深300历史成份股，包括成份股张跌幅和权重

wind说明：
    用到的wind内部函数有:w.wsd,w.wset




'''

import pandas as pd
from WindPy import w
w.start()

windcode = '000300.SH'
daystart = '2005-04-01'
dayend = '2017-12-19'
daystrade = w.tdays(daystart,dayend)


#data = w.wsd('000001.SZ','close',dayend,dayend)

dfhs300code = pd.DataFrame()
dfhs300weight = pd.DataFrame()

for dayt in daystrade:
    ## 获取当日沪深300成分股及权重
    date_code = 'date=' + dayt + ';windcode=' + windcode
    w_wset_data = w.wset('indexconstituent',date_code)
    dfwset = pd.DataFrame(w_wset_data.Data).T
    dfwset.columns = w_wset_data.Fields


