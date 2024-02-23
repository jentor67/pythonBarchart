#!/usr/bin/python3
# import library
import numpy as np
from matplotlib import pyplot as plt
from icecream import ic

def main():

    timeOfNote=[0,1,4,5,6,7,10,12,13,16,20,21,22,23,27,28,29,30,31,35] 
    loudnessOfNote=[0,1,1,8,6,7,5,5,7,2,2,3,3,1,2,3,9,9,3,3] 
    lengthOfNote=[2,1,3,2,2,1,1,2,2,1,1,1,3,3,2,1,1,1,1,2]

    
    # Compute pie slices
    N = 20
    theta = [(i/36)*2*np.pi for i in timeOfNote]
    width = [(i/36)*2*np.pi for i in lengthOfNote]
    colors = plt.cm.viridis(np.array(loudnessOfNote) / 10)
    
    ax = plt.subplot(projection='polar')
    ic(theta)
    print(" ")
    ic(loudnessOfNote)
    print(" ")
    ic(width)
    print(" ")
    ic(colors)

    ax.bar(theta, loudnessOfNote, width=width, bottom=0.0, \
            color=colors, alpha=0.5)
    
    plt.show()

if __name__ == '__main__':
    main()
