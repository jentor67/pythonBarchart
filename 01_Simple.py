#!/usr/bin/python3
# import library
from matplotlib import pyplot as plt
from icecream import ic


def main():
    # Define x axis values
    x=["One","Two","Three","Four"]

    # Define y axis values
    y=[120,150,100,99]

    ic(y)

    # Create bar chart
    plt.bar(x,y)

    plt.xlabel("X label", fontsize = 15)
    plt.ylabel("Y label", fontweight = 'bold', fontsize = 12)
    plt.title("Simple barchart using matplotlib", fontsize = 20)

    # Show plot
    plt.show()

if __name__ == '__main__':
    main()

