import time
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

sys.setrecursionlimit(20000)

# Implementation of Quick Sort Partition
def partition(array, low, high):
    # DEBUG
    # curr = low
    # while(curr < high):
    #     print(f"[{array[curr]}]", end="")
    #     curr += 1
    # print("")
    
    # choose the rightmost element as pivot
    pivot = array[high]   

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            
            i = i + 1
            
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1

# Function to perform QuickSort
def quicksort(array, low, high):
    if low < high:
        
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)
        
# Function for Timing, Takes an integer input, returns the time that took to sort the array of integer size.
def measureQuickSortTime(array_size):
    
    # Creates a Reversed Array from 0 to N.
    array = list(range(0, array_size))
    array.reverse()
    
    # Start Timer
    start = time.perf_counter()
    quicksort(array, 0, len(array) - 1)
    # Stop Timer
    stop = time.perf_counter()
    
    # Get Time
    avg_time = stop - start
    
    # DEBUG
    # print(f"For an array size of {array_size}, average quick_sort takes {avg_time} seconds")
    # print(array)
    return avg_time


# Function for Curve Fitting
def n_squared_model(x, a, b):
    return a * x ** 2 + b




# Array Sizes
array_sizes = [i ** 2 for i in range(0,20)]

# Empty Array to keep the times
times = []

# for loop that calls Timing function for different sizes
for size in array_sizes:
    times.append(measureQuickSortTime(size))

# Plotting  
params_quick, _ = curve_fit(n_squared_model, array_sizes, times)

fig, axs = plt.subplots(nrows=1, ncols=1, figsize= (10, 5))

quick = axs

quick.scatter(array_sizes, times, label='QuickSort', color='g')
quick.plot(array_sizes, n_squared_model(np.array(array_sizes), *params_quick), label='QuickSort Sort Line', color='g')

quick.set_title('QuickSort Times')
quick.set_xlabel('Array Size')
quick.set_ylabel('Time (Seconds)')

quick.legend()

plt.tight_layout()
plt.show()