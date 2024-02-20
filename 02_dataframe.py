#!/usr/bin/python3
# import library
import pandas as pd
from matplotlib import pyplot as plt


def main():
    # Read csv into pandas
    dataFrame = pd.read_csv("testData.csv")
    
    
    # Create bar chart
    plt.bar(dataFrame['X-Values'],dataFrame['Y-Values'])
    
    plt.xlabel("dataFrame X label", fontsize = 15)
    plt.ylabel("Y label", fontweight = 'bold', fontsize = 12)
    plt.title("Simple barchart using matplotlib and pandas", \
            fontweight = 'bold', fontsize = 16)
    
    # Show plot
    plt.show()


if __name__ == '__main__':
    main()
