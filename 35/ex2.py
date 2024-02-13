# Group 35 #
# Ex 2 #

import sys
sys.setrecursionlimit(20_000) # Changing the recursion limit to avoid RecursionError

import time
import random
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Bubble Sort Implementation

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

# Quick Sort Implementation

def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index)
        quickSort(arr, pivot_index + 1, high)

def partition(arr, low, high):

    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right

# Finding decent array sizes that scale decently

array_sizes = [i ** 3 for i in range(1, 21)]

# Measuring Bubble Sort

def measureAverageBubbleSort(array_size):
    
    array = [i for i in range(1, array_size + 1)]
    random.shuffle(array) # Shuffling the array

    start = time.perf_counter()
    bubbleSort(array)
    stop = time.perf_counter()
    avg_time = stop - start

    return avg_time

def measureBestBubbleSort(array_size):

    array = [i for i in range(1, array_size + 1)]
    start = time.perf_counter()
    bubbleSort(array)
    stop = time.perf_counter()
    avg_time = stop - start

    return avg_time

def measureWorstBubbleSort(array_size):

    array = [array_size - i for i in range(1, array_size + 1)]
    start = time.perf_counter()
    bubbleSort(array)
    stop = time.perf_counter()
    avg_time = stop - start

    return avg_time

bubble_best_times = []
for size in array_sizes:
    bubble_best_times.append(measureBestBubbleSort(size))

bubble_average_times = []
for size in array_sizes:
    bubble_average_times.append(measureAverageBubbleSort(size))

bubble_worst_times = []
for size in array_sizes:
    bubble_worst_times.append(measureWorstBubbleSort(size))

# Measuring Quick Sort

def measureBestQuickSort(array_size):
    
    array = [i for i in range(1, array_size + 1)]
    random.shuffle(array)

    start = time.perf_counter()
    quickSort(array, 0, array_size - 1)
    stop = time.perf_counter()
    avg_time = stop - start

    return avg_time

def measureAverageQuickSort(array_size):

    array = [i for i in range(1, array_size + 1)]
    random.shuffle(array)

    start = time.perf_counter()
    quickSort(array, 0, array_size - 1)
    stop = time.perf_counter()
    avg_time = stop - start

    return avg_time

def measureWorstQuickSort(array_size):

    array = [i for i in range(1, array_size + 1)]

    start = time.perf_counter()
    quickSort(array, 0, array_size - 1)
    stop = time.perf_counter()
    avg_time = stop - start

    return avg_time

quick_best_times = []
for size in array_sizes:
    quick_best_times.append(measureBestQuickSort(size))

quick_average_times = []
for size in array_sizes:
    quick_average_times.append(measureBestQuickSort(size))

quick_worst_times = []
for size in array_sizes:
    quick_worst_times.append(measureBestQuickSort(size))

# Curve Fitting

def nSquaredModel(x, a, b):
    return a * x ** 2 + b

def nlognModel(x, a, b):
    return a * (x * np.log(x)) + b

params_bubble_average, _ = curve_fit(nSquaredModel, array_sizes, bubble_average_times)
params_bubble_worst, _ = curve_fit(nSquaredModel, array_sizes, bubble_worst_times)
params_bubble_best, _ = curve_fit(nSquaredModel, array_sizes, bubble_best_times)

params_quick_average, _ = curve_fit(nlognModel, array_sizes, quick_average_times)
params_quick_worst, _ = curve_fit(nSquaredModel, array_sizes, quick_worst_times)
params_quick_best, _ = curve_fit(nlognModel, array_sizes, quick_best_times)

# Plotting

fig, axs = plt.subplots(nrows=1, ncols=2, figsize= (15, 5))

bubble = axs[0]
quick = axs[1]

# Bubble Sort Plot
bubble.scatter(array_sizes, bubble_best_times, label='best', color= 'red')
bubble.plot(array_sizes, nSquaredModel(np.array(array_sizes), *params_bubble_best), label='best line', color='red')

bubble.scatter(array_sizes, bubble_average_times, label='average', color= 'blue')
bubble.plot(array_sizes, nSquaredModel(np.array(array_sizes), *params_bubble_average), label='average line', color='blue')

bubble.scatter(array_sizes, bubble_worst_times, label='worst', color= 'green')
bubble.plot(array_sizes, nSquaredModel(np.array(array_sizes), *params_bubble_worst), label='worst line', color='green')

# Quick Sort Plot
quick.scatter(array_sizes, quick_best_times, label='best', color= 'red')
quick.plot(array_sizes, nlognModel(np.array(array_sizes), *params_quick_best), label='best line', color='red')

quick.scatter(array_sizes, quick_average_times, label='average', color= 'blue')
quick.plot(array_sizes, nlognModel(np.array(array_sizes), *params_quick_average), label='average line', color='blue')

quick.scatter(array_sizes, quick_worst_times, label='worst', color= 'green')
quick.plot(array_sizes, nSquaredModel(np.array(array_sizes), *params_quick_worst), label='worst line', color='green')

bubble.set_title('Bubble Sort Best Case Performance')
bubble.set_xlabel("Array Size")
bubble.set_ylabel("Time (seconds)")

quick.set_title('Quick Sort Best Case Performance')
quick.set_xlabel("Array Size")
quick.set_ylabel("Time (seconds)")

bubble.legend()
quick.legend()

plt.tight_layout()
plt.show()