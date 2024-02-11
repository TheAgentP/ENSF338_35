# Group 35
# ex 5

import matplotlib.pyplot as plt
import random
import time
import numpy as np
from scipy.optimize import curve_fit

# Tradition Insertion Sort Implementation
def insertion_sort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

# Binary Insertion Sort Implementation
def binary_search(a, item, low, high):
	while (low <= high):
		mid = low + (high - low) // 2
		if (item == a[mid]):
			return mid + 1
		elif (item > a[mid]):
			low = mid + 1
		else:
			high = mid - 1
	return low
	
# Function to sort an array a[] of size 'n'
def binary_insertion_sort(a, n):
	for i in range (n): 
		j = i - 1
		selected = a[i]
		
		# find location where selected should be inserted
		loc = binary_search(a, selected, 0, j)
		
		# Move all elements after location to create space
		while (j >= loc):
			a[j + 1] = a[j]
			j-=1
		a[j + 1] = selected

# Finding decent array sizes that scale decently
array_sizes = [i ** 2 for i in range(20)]

# Measure Insertion Sort
def measureInsertionSort(array_size):

    array = [random.randint(0, array_size) for _ in range(array_size)]
    start = time.perf_counter()
    insertion_sort(array)
    stop = time.perf_counter()
    avg_time = stop - start
    # # DEBUG
    # print(f"For an array size of {array_size}, average insertion_sort takes {avg_time} seconds")
    # print(array)

    return avg_time

# Measure Binary Sort
def measureBinaryInsertionSort(array_size):

    array = [random.randint(0, array_size) for _ in range(array_size)]
    start = time.perf_counter()
    binary_insertion_sort(array, len(array))
    stop = time.perf_counter()
    avg_time = stop - start
    # DEBUG
    # print(f"For an array size of {array_size}, average binary_insertion_sort takes {avg_time} seconds")
    # print(array)

    return avg_time

insertion_sort_times = []
for size in array_sizes:
    insertion_sort_times.append(measureInsertionSort(size))

binary_insertion_sort_times = []
for size in array_sizes:
    binary_insertion_sort_times.append(measureBinaryInsertionSort(size))


# Curve fitting
def n_squared_model(x, a, b):
    return a * x ** 2 + b

params_insertion, _ = curve_fit(n_squared_model, array_sizes, insertion_sort_times)
params_binary_insertion, _ = curve_fit(n_squared_model, array_sizes, binary_insertion_sort_times)

fig, axs = plt.subplots(nrows=1, ncols=1, figsize= (10, 5))
insertion = axs

# Plotting insertion sorts
insertion.scatter(array_sizes, insertion_sort_times, label= 'Insertion sort', color= 'red')
insertion.plot(array_sizes, n_squared_model(np.array(array_sizes), *params_insertion), label= 'Insertion sort line', color= 'red')

insertion.scatter(array_sizes, binary_insertion_sort_times, label= 'Binary insertion sort', color= 'blue')
insertion.plot(array_sizes, n_squared_model(np.array(array_sizes), *params_binary_insertion), label= 'Binary insertion sort line', color= 'blue')

insertion.set_title('Traditional and Binary Insertion Sort')
insertion.set_xlabel("Array Size")
insertion.set_ylabel("Time (seconds)")

insertion.legend()

plt.tight_layout()
plt.show()

# Q4.
# Binary Insertion Sort (BIS) and Traditional Insertion Sort (TIS) take about the same time. 
# Even though BIS utilizes Binary Search as a means to try to optimize the function, it's only a search. 
# Consequently, the BIS algorithm still has to insert the key into the found spot which 
# involves shifting all the elements to the right, an O(n) operation. 
# This leads to BIS having a complexity of O(n^2), the same as TIS.