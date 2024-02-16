#!/usr/bin/python3
# import library
from matplotlib import pyplot as plt

# Define x axis values
x=["One","Two","Three","Four"]

# Define y axis values
y=[120,150,100,99]

# Create bar chart
plt.bar(x,y)

plt.xlabel("X label", fontsize = 15)
plt.ylabel("Y label", fontweight = 'bold', fontsize = 12)
plt.title("Simple barchart using matplotlib", fontsize = 20)

# Show plot
plt.show()

