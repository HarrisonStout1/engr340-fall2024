
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

### Your code here ###
df = np.loadtxt(path, delimiter=",", skiprows=2)
time = df[:,0]
mlii = df[:,1]
v1 = df[:,2]


plt.plot(time,mlii,label="mlii")
plt.plot(time,v1,label="V1")
plt.title("EKG Plot")
plt.xlabel("Time [Seconds]")
plt.ylabel("Lead Voltage [mV]")
plt.legend()
plt.show()
# save each vector as own variable

### Your code here ###

# use matplot lib to generate a single

### Your code here ###