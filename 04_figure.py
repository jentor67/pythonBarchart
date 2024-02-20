#!/usr/bin/python3
# import library
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def main():
    # Read csv into pandas
    dataFrame = pd.read_csv("testData.csv")
    
    
    fig, ax = plt.subplots(figsize = (10,6))
    
    ax.bar( dataFrame['X-Values'], dataFrame['Y-Values'])
    ax.set_ylim(0,100)
    
    ax2 = ax.twinx()
    ax2.set_ylim(0,2100)
    ax2.plot( dataFrame['X-Values'], dataFrame['LineValue'], color='green')
    
    # add titles
    ax.set_xlabel( "dataFrame X label", fontsize = 15)
    ax.set_ylabel( "Y label", fontweight = 'bold', fontsize = 12)
    ax2.set_ylabel( "Y line label", fontweight = 'bold', fontsize = 12)
    ax.set_title( "Barchart using a figures", \
            fontweight = 'bold', fontsize = 16)
    
    # watermark text
    fig.text(.95,.025,'Test watermark', fontsize = 14, \
            fontweight = 'bold', color='red', \
            ha='right', va='bottom', alpha = .5)
    
    # Show plot
    plt.show()

if __name__ == '__main__':
    main()
