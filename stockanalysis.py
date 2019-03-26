import tushare as ts
import urllib
import re

print(5)

def urlTolist(url): 
    allCodeList = []
     html = urllib.request.urlopen(url).read()
     html = html.decode('gbk') 
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">' 
    pat = re.compile(s)
     code = pat.findall(html)
     for item in code: 
        if item[0] == '6' or item[0] == '3' or item[0] == '0': 
            allCodeList.append(item) 
    return allCodeList

print((urlTolist("http://quote.eastmoney.com/stocklist.html")))

# ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')
