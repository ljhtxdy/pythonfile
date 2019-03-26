import tushare as ts
import os
import numpy


filename = 'c:/bigfile.csv'


ts.set_token("3e3ed9ba576210c210d0aa08959fdd3b32de36515af178850f05e151")

pro = ts.pro_api()

data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

allcode=data['symbol'].values.tolist()

for a in allcode:
    b=ts.get_h_data(a, start='2018-08-01', end='2019-03-26')
    closeprice=b['close'].values.tolist()
    narray=numpy.array(closeprice)
    sum1=narray.sum()
    narray2=narray*narray
    sum2=narray2.sum()
    N=len(closeprice)
    mean=sum1/N
    var=sum2/N-mean**2
    print(var^0.5)
