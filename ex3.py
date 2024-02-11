# Group 35
# Ex 3

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Implementation of Bubble Sort
def bubble_sort(a):
    n = len(a)
    global comps
    comps = 0
    global swaps
    swaps = 0
    for i in range(n):
        comps += 1
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swaps += 1
    print ("comparisons made - ", comps)
    print ("swaps made - ", swaps)
    return a, swaps, comps

# Testing with array sizes
totalswaps = []
totalcompares = []
arraylen = []

array = [6,3,8,5]
bubble_sort(array)
print (array)
totalswaps.append (swaps)
totalcompares.append (comps)
arraylen.append (len(array))

array2 = [12,4,89,4,312,7]
bubble_sort(array2)
print (array2)
totalswaps.append (swaps)
totalcompares.append (comps)
arraylen.append (len(array2))

array3 = [78,34,65,12,67,90,12,43]
bubble_sort(array3)
print (array3)
totalswaps.append (swaps)
totalcompares.append (comps)
arraylen.append (len(array3))

array4 = [49,43,54,63,77,12,99,17,33,44]
bubble_sort(array4)
print (array4)
totalswaps.append (swaps)
totalcompares.append (comps)
arraylen.append (len(array4))

array5 = [21,3,5,11,76,12,89,56,67,88,44,28]
bubble_sort(array5)
print (array5)
totalswaps.append (swaps)
totalcompares.append (comps)
arraylen.append (len(array5))

# Curve fitting model
def n_squared_model(x, a, b):
    return a * x ** 2 + b

params_comparisons, _ = curve_fit(n_squared_model, arraylen, totalcompares)
params_swaps, _ = curve_fit(n_squared_model, arraylen, totalswaps)

fig, axs = plt.subplots(nrows=1, ncols=1, figsize= (9, 5))
bubble = axs

# comparisons and swaps plot 
bubble.scatter(arraylen, totalcompares, label='Comparison Times', color= 'red')
bubble.plot(arraylen, n_squared_model(np.array(arraylen), *params_comparisons), label= 'Comparions Fitted Line', color= 'red')

bubble.scatter(arraylen, totalswaps, label='Swaps Times', color= 'blue')
bubble.plot(arraylen, n_squared_model(np.array(arraylen), *params_swaps), label= 'Swaps Fitted Line', color= 'blue')


bubble.set_title('Plot of Comparisons and Swaps')
bubble.set_xlabel("Array Size")
bubble.set_ylabel("Time (seconds)")

bubble.legend()

plt.tight_layout()
plt.show()