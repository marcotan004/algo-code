import random
import math
def initializeArray(m,n, bound):
    array = [[random.randint(0,bound) for i in range(n)] for i in range(m)]
    for i in array:
        i.sort()
    
    return array

def mergeArrays(array1, array2):
    p1 = 0
    p2 = 0
    count = 0
    
    returned = [0]*(len(array1)+len(array2))

    while p1 < len(array1) and p2 < len(array2):
        if array1[p1] <= array2[p2]:
            returned[count] = array1[p1]
            p1 += 1
            count += 1
        else:
            returned[count] = array2[p2]
            p2 += 1
            count += 1
    
    if p1 < len(array1):
        returned[count:] = array1[p1:]
    
    elif p2 < len(array2):
        returned[count:] = array2[p2:]

    return returned

def mergeKLists(array):
    #print('Array length: {0}'.format(len(array)))
    #print('Array: {0}'.format(array))
    if len(array) == 1:
        return array[0]
    elif len(array) == 0:
        return []
    
    middle = math.floor((len(array)-1)/2)
    array1 = mergeKLists(array[0:middle+1])
    array2 = mergeKLists(array[middle+1:len(array)])

    return mergeArrays(array1, array2)

m = 7
n = 6
bound = 150
initialArray = initializeArray(m,n,bound)
print(initialArray)
result = mergeKLists(initialArray)
print('Result: {0}'.format(result))
print(len(result))