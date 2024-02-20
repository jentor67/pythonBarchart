#!/usr/bin/python3
# import library
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def main():
    # Read csv into pandas
    dataFrame = pd.read_csv("testData.csv")

    # 2 subplots
    fig, ax = plt.subplots(2)
    
    # first chart
    ax[0].bar( dataFrame['X-Values'], dataFrame['Y-Values'])
    ax[0].set_xlabel("data Frame X label", fontsize = 10)
    ax[0].set_ylabel("data Frame Y label", fontsize = 10)
    ax[0].set_title("X vs y", fontweight = 'bold', fontsize = 15)

    # second chart
    ax[1].bar( dataFrame['X-Values'], dataFrame['Y2-Values'])
    ax[1].set_xlabel("data Frame X label", fontsize = 10)
    ax[1].set_ylabel("data Frame Y2 label", fontsize = 10)
    ax[1].set_title("X vs y2", fontweight = 'bold', fontsize = 15)


    fig.tight_layout(pad=1.0)

    plt.show()

if __name__ == '__main__':
    main()
