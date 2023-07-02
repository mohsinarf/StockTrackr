import yfinance as yf

import matplotlib.pyplot as plt
import seaborn

if __name__ == "__main__":
    msft = yf.Ticker("MSFT")

    # get stock info
    print(msft.info)

    # get historical market data
    hist = msft.history(period="5d")
        
        
    data_df = yf.download("AAPL", start="2020-02-01", end="2020-03-20")
    data_df.to_csv('aapl.csv')
    # x axis values
    x = [1,2,3]
    # corresponding y axis values
    y = [2,4,1]
    
    # plotting the points 
    plt.plot(x, y)
    
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    
    # giving a title to my graph
    plt.title('My first graph!')
    
    # function to show the plot
    plt.show()

