#!/usr/bin/python3
# import library
from matplotlib import pyplot as plt
import numpy as np
from icecream import ic


def gradientbars(bars):
    npLine = np.linspace(0,1,256)
    grad = np.atleast_2d(npLine).T
    ax = bars[0].axes
    lim = ax.get_xlim()+ax.get_ylim()
    zord=1
    for bar in bars:
        bar.set_zorder(1)
        bar.set_facecolor('none')
        x,y = bar.get_xy()
        w, h = bar.get_width(), bar.get_height()
        ax.imshow(grad, extent=[x,x+w,y,y+h], aspect='auto', zorder=zord)
        zord += 10
        ic(zord)
    ax.axis(lim)

def main():
    # Define x axis values
    x=["One","Two","Three","Four"]

    # Define y axis values
    y=[120,150,100,99]

    # Create bar chart
    bar = plt.bar(x,y)


    gradientbars(bar)

    plt.xlabel("X label", fontsize = 15)
    plt.ylabel("Y label", fontweight = 'bold', fontsize = 12)
    plt.title("Simple barchart using matplotlib", fontsize = 20)

    # Show plot
    plt.show()

if __name__ == '__main__':
    main()

