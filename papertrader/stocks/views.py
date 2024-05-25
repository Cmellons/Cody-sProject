from django.shortcuts import render
import requests
# Create your views here.
# 15min, 30min, 60min will not work with Demo key
def index(request):
    name = 'PaperTrader'
    stock_name = 'IBM'
    time_frame = '1D'
    if 'stockname' in request.POST:
        stock_name = request.POST['stockname']
        print(stock_name)
    if '1min' in request.POST:
        time_frame = '1min'
    elif '5min' in request.POST:
        time_frame = '5min'
    elif '15min' in request.POST:
        time_frame = '15min'
    elif '30min' in request.POST:
        time_frame = '30min'
    elif '60min' in request.POST:
        time_frame = '60min'
    elif '1D' in request.POST:
        time_frame = '1D'
    elif '1W' in request.POST:
        time_frame = '1W'
    elif '1Y' in request.POST:
        time_frame = '1Y'
    def get_stock_data(stock_name, time_frame):
        if time_frame in ('1min', '5min', '15min', '60min'):
            URL = 'https://www.alphavantage.co/query'
            PARAMS = {'function':'TIME_SERIES_INTRADAY',
                'symbol':stock_name,
                'interval':time_frame,
                'apikey': 'demo' #demo to work for now. use your key only 25times a day.
               }
            time_frame_string = 'Time Series ('+time_frame +')'
        elif time_frame in ('1D'):
            URL = 'https://www.alphavantage.co/query'
            PARAMS = {'function':'TIME_SERIES_DAILY',
             'symbol':stock_name,
            'apikey': 'demo' #use your key instead of demo but only
               }
            time_frame_string = 'Time Series (Daily)'
        elif time_frame in ('1W'):
            URL = 'https://www.alphavantage.co/query'
            PARAMS = {'function':'TIME_SERIES_WEEKLY',
             'symbol':stock_name,
            'apikey': 'demo' #use your key instead of demo but only
               }
            time_frame_string = 'Weekly Time Series'
        elif time_frame in ('1M'):
            URL = 'https://www.alphavantage.co/query'
            PARAMS = {'function':'TIME_SERIES_MONTHLY',
             'symbol':stock_name,
            'apikey': 'demo' #use your key instead of demo but only
               }
            time_frame_string = 'Monthly Time Series'
        req = requests.get(url=URL, params= PARAMS)
        data = req.json()
        print(data)
        stock_data = data[time_frame_string]
        data_keys = list(data[time_frame_string].keys())
        dataset = []
        for cnt, item in enumerate(data[time_frame_string]):
            sets = {'label': data_keys[cnt],
                'y': [round(float(data[time_frame_string][item]['1. open']),2),
                      round(float(data[time_frame_string][item]['2. high']),2),
                      round(float(data[time_frame_string][item]['3. low']),2),
                      round(float(data[time_frame_string][item]['4. close']),2)]
                }
            dataset.append(sets)
        return dataset[::-1]
    dataset = get_stock_data(stock_name,time_frame)
    return render(request, 'stocks/index.html', {'name':stock_name,
                                                 'stockname': stock_name,
                                                 'time_frame':time_frame,
                                                 'data':dataset[-30:]})
