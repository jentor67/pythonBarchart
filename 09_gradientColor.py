#!/usr/bin/python3
# import library
from matplotlib import pyplot as plt
import numpy as np
from icecream import ic


def gradientbars(bars):
    ##### gradient prep#####
    # create array from 0 to 1 with subdivision of 256
    npLine = np.linspace(0,1,256)

    # takes an 1 by n array and make it a n x1 array
    # [1,n] --> [[1,n]] --> [[n,1]]
    grad = np.atleast_2d(npLine).T
    #######################
   
    # axis of the barplot bars 
    ax = bars[0].axes

    ## canvas (xmin, xmax, ymin, ymax)
    lim = ax.get_xlim()+ax.get_ylim()

    for bar in bars:
        # get the x and y position
        x,y = bar.get_xy()

        # get width height of bar
        w, h = bar.get_width(), bar.get_height()

        # create a square with grad gradient
        # zorder is not applicable but we still need it
        ax.imshow(grad, extent=[x,x+w,y,y+h], aspect='auto', zorder=1)

    ax.axis(lim)



def main():
    # Define x axis values
    x=["One","Two","Three","Four"]

    # Define y axis values
    y=[120,150,100,30]

    # Create bar chart
    bar = plt.bar(x,y)


    #gradientbars(bar)

    plt.xlabel("X label", fontsize = 15)
    plt.ylabel("Y label", fontweight = 'bold', fontsize = 12)
    plt.title("Simple barchart using matplotlib", fontsize = 20)

    # Show plot
    plt.show()

if __name__ == '__main__':
    main()

