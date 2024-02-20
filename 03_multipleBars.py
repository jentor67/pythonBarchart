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
    x1 = np.arange(len(dataFrame['X-Values']))
    x2 = [x + barWidth for x in x1]
    x3 = [x + barWidth for x in x2]
    
    # Create bar chart
    plt.bar(x1,dataFrame['Y-Values'], width = barWidth, \
            label='Y-Values')
    plt.bar(x2,dataFrame['Y2-Values'], width = barWidth, \
            label='Y1-Values')
    plt.bar(x3,dataFrame['Y3-Values'], width = barWidth, \
            label='Y2-Values')
    
    plt.xlabel("dataFrame X label", fontsize = 15)
    plt.ylabel("Y label", fontweight = 'bold', fontsize = 12)
    plt.title("Multiple bars", \
            fontweight = 'bold', fontsize = 16)
    # show legen
    plt.legend()
    
    # Show plot
    plt.show()

if __name__ == '__main__':
    main()
