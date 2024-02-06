import matplotlib.pyplot as pyplot

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

pyplot.plot (arraylen, totalswaps)
pyplot.plot (arraylen, totalcompares)
pyplot.show()


