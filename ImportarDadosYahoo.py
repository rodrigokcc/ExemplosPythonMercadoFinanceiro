import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()

inicio=dt.datetime(2020,1,1)
fim=dt.datetime(2021,2,5)

aapl= yf.Ticker("^bvsp").history(start=inicio,end=fim)

close_prices = aapl['Close']
dates = aapl.index
plt.plot(dates, close_prices)
plt.xticks(dates)
plt.gca().set_xticklabels(dates.strftime('%d'))
plt.xticks(dates[::20])
plt.show()
