import matplotlib.pyplot as plt
import random
import time
import numpy as np
from scipy.optimize import curve_fit
from statistics import mean
import sys
from statistics import mean
sys.setrecursionlimit(20000)

# Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

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

# Measure Times
def linear_time(array_size, key):
    linear_times = []
    # Creates an Array of Appropriate Size and Shuffles It
    array = list(range(0,array_size))
    random.shuffle(array)
    
    # Gets a list of times
    for _ in range(0, 100):
        start = time.perf_counter()
        linear_search(array, key)
        end = time.perf_counter()
        linear_times.append(end - start)
        random.shuffle(array)
    return mean(linear_times)

def quickBinarySearch(array_size, key):
    quickb_times = []
    
    # Creates an Array of Appropriate Size and Shuffles It
    array = list(range(0, array_size))
    random.shuffle(array)

    for _ in range(0, 100):
        start = time.perf_counter()
        quickSort(array, 0, len(array) - 1)
        # DEBUG
        # print(array)
        # print(f"Found {key} at {binary_search(array, 0, len(array) - 1, key)}")
        binary_search(array, 0, len(array) - 1, key)
        end = time.perf_counter()
        quickb_times.append(end - start)
        random.shuffle(array)
    return mean(quickb_times)

array_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
# array_sizes = [i ** 2 for i in range(1, 100)] # DEBUG
key = 7

linearSearch_times = []
quickBinary_times = []

for i in array_sizes:
    linearSearch_times.append(linear_time(i, key))

for i in array_sizes:
    quickBinary_times.append(quickBinarySearch(i, key))

# DEBUG
# quickBinarySearch(20, 7)

# Curve fitting
def linear_model(x, a, b):
    return a * x + b

def n_squared_model(x, a, b):
    return a * x ** 2 + b

def n_log_n_model(x, a, b):
    return a * (x * np.log(x * b))

params_linear, _ = curve_fit(linear_model, array_sizes, linearSearch_times)
params_quick_binary, _ = curve_fit(n_log_n_model, array_sizes, quickBinary_times)

# Plotting
fig, axs = plt.subplots(nrows=1, ncols=2, figsize= (15, 5))

linear = axs[0]
quickbinary = axs[1]

# Plotting insertion sorts
linear.scatter(array_sizes, linearSearch_times, label= 'Linear Times', color= 'red')
linear.plot(array_sizes, linear_model(np.array(array_sizes), *params_linear), label= 'Linear Search line', color= 'red')

quickbinary.scatter(array_sizes, quickBinary_times, label= 'Quick Sort & Binary Times', color= 'blue')
quickbinary.plot(array_sizes, n_log_n_model(np.array(array_sizes), *params_quick_binary), label= 'Quick Sort & Binary Search line', color= 'blue')

linear.set_title('Plot of Linear Search')
linear.set_xlabel("Array Size")
linear.set_ylabel("Time (seconds)")

quickbinary.set_title('Plot of Quick Sort and Binary Search')
quickbinary.set_xlabel("Array Size")
quickbinary.set_ylabel("Time (seconds)")

linear.legend()
quickbinary.legend()

plt.tight_layout()
plt.show()

# Q4
# The Linear Search has a standard O(n) complexity. 
# In our findings, the combination of Quick Sort and Binary Search has a best fit line that matches O(n log(n)). 
# This coincides with the average case complexity for a Quick Sort. 
# However, as seen from the plots, linear search is a lot faster because it doesn't have to sort prior to searching the array.