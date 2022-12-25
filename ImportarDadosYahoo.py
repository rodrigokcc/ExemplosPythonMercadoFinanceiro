import matplotlib.pyplot as fig
import datetime as dt
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()

inicio=dt.datetime(2020,1,1)
fim=dt.datetime(2021,2,5)

aapl= yf.Ticker("^bvsp").history(start=inicio,end=fim)

print(aapl)


#df=web.DataReader('MSFT','yahoo',inicio,fim)


x = aapl['Close']
print(x)
fig.plot(aapl)
fig.show()
