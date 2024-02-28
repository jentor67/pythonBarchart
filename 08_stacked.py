#!/usr/bin/python3
# import library
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def main():

    # Read csv into pandas
    dataFrame = pd.read_csv("testData.csv")
    
    # set barwidth
    barWidth = .25
    
    # set postion of bar on x axis
    x = np.arange(len(dataFrame['X-Values']))
  
    # assign values to variables
    Y = dataFrame['Y-Values']
    Y2 = dataFrame['Y2-Values']
    Y3 = dataFrame['Y3-Values']

    # Heights of Y + Y2
    bars = np.add(Y,Y2).tolist()

    # Create bar chart
    plt.bar(x, Y, width = barWidth, label = 'Y-Values')
    plt.bar(x, Y2, bottom = Y, width = barWidth, label = 'Y1-Values')
    plt.bar(x, Y3, bottom = bars, width = barWidth, label = 'Y2-Values')
    
    plt.xlabel("dataFrame X label", fontsize = 15)
    plt.ylabel("Y label", fontweight = 'bold', fontsize = 12)
    plt.title("Stacked bars", fontweight = 'bold', fontsize = 16)

    # Extend the y-axis
    plt.ylim(0,150)
    # show legen
    plt.legend()
    
    # Show plot
    plt.show()

if __name__ == '__main__':
    main()
