#!/usr/bin/python3
# import library
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from icecream import ic


def main():

    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')

    # create number 0 - 5 step 1
    start = .1
    end = 10
    step = .1
    x = np.arange(start, end + step, step)
  
    # List of Battery ratings
    equations = ['.1x^2','x^2-8x+10','.01x^3','-.25i^3+4x^2-15x+11','x']
 
    Y = np.empty((0,5))

    for i in x:
        line =[]
        line.append(.1*i**2)
        line.append(i**2 -8*i +10 )
        line.append(.01*i**3)
        line.append(-.25*i**3 + 4*i**2 - 15*i +11)
        line.append(i)
        Y = np.vstack((Y,np.array(line))) 


    # Represent battery rating in numeric codes
    yticks = [0, 1, 2, 3, 4]
    
    # Use different color for each of the battery ratings
    colors = ['r', 'g', 'b', 'y', 'm']
    
    i=0
    for c, k in zip(colors, yticks):
        cs = [c] * len(x)
        ax.bar(x, Y[:,i], width = .8*step, zs=k, zdir='y', color=cs, \
                alpha=0.7)
        i += 1

    ax.set_yticks(yticks)
    ax.set_yticklabels(equations)
    ax.set_xlabel('X')
    ax.set_ylabel('Equations')
    ax.set_zlabel('Y value')


    # Show plot
    plt.show()



if __name__ == '__main__':
    main()

