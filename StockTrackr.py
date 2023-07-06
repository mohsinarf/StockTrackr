from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import requests
import os

def main():
    ts = TimeSeries(key='ALPHAVANTAGE_API_KEY')
    data, meta_data = ts.get_daily(symbol='AAPL', outputsize='full')

    # Extract the dates and closing prices from the data
    dates = []
    closing_prices = []

    # Data is returned in reverse chronological order, so we iterate in reverse
    for date in reversed(list(data.keys())):
        dates.append(date)
        closing_prices.append(float(data[date]['4. close']))

# Plotting the data
    plt.plot(dates, closing_prices)
    plt.xlabel('Date')
    plt.ylabel('Closing Price ($)')
    plt.title('AAPL Stock Price')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


