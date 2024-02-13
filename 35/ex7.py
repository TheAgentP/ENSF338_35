# Group 35
# ex7

import json

def binary_search (d_l, t):
    low = 0
    high = len(d_l) - 1


    while low <= high:
        midpoint = (low + high) // 2
        mid_num = d_l[midpoint]

        if mid_num == t:
            return mid_num
        elif mid_num < t:
            low = mid_num + 1
        else:
            high = mid_num - 1

with open('ex7data.json', 'r' ) as datafile:
    data = json.load(datafile)

with open('ex7tasks.json', 'r' ) as taskfile:
    taskdata = json.load(taskfile)


result = {}
for searchnum in taskdata:
    index = binary_search(data, searchnum)
    result[searchnum] = index

for searchnum, main_find in result.items():
    if index != -1:
        print (f'Task Number {searchnum} found')        
    else:
        print (f'{searchnum} Not Found')