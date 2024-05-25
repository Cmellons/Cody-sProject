from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    name = 'PaperTrader'
    stock_name = 'IBM'
    URL = 'https://www.alphavantage.co/query'
    PARAMS = {'function':'TIME_SERIES_INTRADAY',
             'symbol':stock_name,
              'interval': '1min',
               'apikey': 'OCCFSGAHASKH9CQ2'}
    req = requests.get(url=URL, params= PARAMS)
    data = req.json()
    return render(request, 'stocks/index.html', {'name':stock_name,
                                                 'stockname': stock_name,
                                                  'data':data })
