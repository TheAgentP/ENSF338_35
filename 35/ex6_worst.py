# Group 35
# ex 6 worst

import matplotlib.pyplot as plt
import random
import time
import numpy as np
from scipy.optimize import curve_fit
from statistics import mean
import sys
from statistics import mean
sys.setrecursionlimit(20000)

# Binary Search
def binary_search(arr, low, high, key):
 
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        
        # If element is present at the middle itself
        if arr[mid] == key:
            return mid
        # be present in left subarray
        elif arr[mid] > key:
            return binary_search(arr, low, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, high, key)
    else:
        return -1

# Quick Sort
def partition(array, low, high):
    
    pivot = array[high]
    
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
  
def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)
        
        quickSort(array, pi + 1, high)

# Measuring times
def worstBinarySearch(array_size, key):
    worstb_times = []
    
    array = list(range(0, array_size))
    array.reverse()
    
    for _ in range(0, 100):
        start = time.perf_counter()
        quickSort(array, 0, len(array) - 1)
        binary_search(array, 0, len(array) - 1, key)
        end = time.perf_counter()
        # DEBUG
        # print(array)
        # print(f"Found {key} at {binary_search(array, 0, len(array) - 1, key)}")
        worstb_times.append(end - start)
        random.shuffle(array)
    return mean(worstb_times)

array_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
# array_sizes = [i ** 2 for i in range(100)] # DEBUG
key = 7
worstBinary_times = []

for i in array_sizes:
    worstBinary_times.append(worstBinarySearch(i, key))

# Curve fitting
def n_squared_model(x, a, b):
    return a * x ** 2 + b

params_worst_binary, _ = curve_fit(n_squared_model, array_sizes, worstBinary_times)

# Plotting
fig, axs = plt.subplots(nrows=1, ncols=1, figsize= (7, 5))

worstbinary = axs

worstbinary.scatter(array_sizes, worstBinary_times, label= 'Quick Sort & Binary Times (Worst)', color= 'blue')
worstbinary.plot(array_sizes, n_squared_model(np.array(array_sizes), *params_worst_binary), label= 'Quick Sort & Binary Search line (Worst)', color= 'blue')

worstbinary.set_title('Plot of Quick Sort and Binary Search (Worst)')
worstbinary.set_xlabel("Array Size")
worstbinary.set_ylabel("Time (seconds)")

worstbinary.legend()

plt.tight_layout()
plt.show()