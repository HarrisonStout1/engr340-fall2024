import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = np.loadtxt(signal_filepath,delimiter=",",skiprows=2)
a1 = signal[:,0] #Elapsed time [s]
a2 = signal[:,1] # MLII [mv]
a3 = signal[:,2] #V1 [mv]



"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""

diffs = np.diff(a2)


"""
Step 4: Square the results of the previous step
"""
square = np.square(a2)

"""
Step 5: Pass a moving filter over your data
"""
vector = np.array([1,1,1,1,1,1,1,1])
scaled = len(vector)
average = (1/len(vector))*vector


moving_filter = np.convolve(square,average)

## YOUR CODE HERE
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
signal = moving_filter
plt.title('Process Signal for ' + database_name)
plt.xlabel("Seconds Elapsed after I squared that hoe")
plt.ylabel("MLII [mV]")
plt.plot(signal)
plt.show()