#!/usr/bin/python3
# import library
import numpy as np
from matplotlib import pyplot as plt
from icecream import ic

def main():
    ## lets assume this is a coffie shop which have hours 
    ## from 6 am - 6 pm but the there is 2 hours of prep in the morning
    ## and 1 hour at night so we have an array from 4 to 7

    ## create an array from 0 to 23 using numpy
    hoursLabel = np.arange(0,24)
    hours = np.arange(4,19)
    ## add 1/2 hour to center
    hours = np.array(hours) + .5

    ## list of employees per hour
    employees = np.array([1,2,2,3,3,3,2,2,3,3,3,2,2,2,2])

    ## list of 10 customers per hour
    customers = (np.array([0,0,2,3,3,2,3,3,2,2,2,3,2,1,0]))*2


    # Compute pie slices of employees
    thetaLabel = [(i/24)*2*np.pi for i in hoursLabel]
    theta = [(i/24)*2*np.pi for i in hours]
    width = [(1/24)*2*np.pi for i in hours]
    colors = 'red'

    ax = plt.subplot(projection='polar')

    ax.bar(theta, employees, width=width, bottom=0.0, \
            color=colors, alpha=0.75, label='Workers')
 
    ax.set_xticks(thetaLabel)
    ax.set_xticklabels(hoursLabel)

    # Compute pie slices of customers
    theta = [(i/24)*2*np.pi for i in hours]
    width = [(1/24)*2*np.pi for i in hours]
    colors = 'green'

    ax1 = plt.subplot(projection='polar')
    
    ax1.bar(theta, customers, width=width, bottom=0.0, \
            color=colors, alpha=0.5, label='Customers')

    plt.title('Number of workders and customers per hour')

    plt.legend(loc='upper right')
    plt.show()

if __name__ == '__main__':
    main()
