import random

x=[random.randint(0,10) for i in range(25)]
rot = [0 for i in range(25)] 
x.sort()

def binarySearch(x, search, low, high):
    if high < low:
        return -1
    
    r = (high + low) // 2

    if search == x[r]:
        return r
    
    if search < x[r]:
        return binarySearch(x, search, low, r-1)
    else:
        return binarySearch(x, search, r+1, high)

def getMax(k, nums):
    return nums[(len(nums) - 1 + k) % len(nums)]

def rotateList(x, rot, k):
    for i in range(len(x)):
        rot[(i + k) % len(x)] = x[i]

def searchForPivot(x,l,r):
    if r < l:
        return -1
    if r == l:
        return l
    
    mid = (l + r) // 2
    if mid > l and x[mid-1] > x[mid]:
        return mid-1
    elif mid < r and x[mid] > x[mid+1]:
        return mid
    
    if x[l] > x[mid]:
        return searchForPivot(x,l,mid-1)
    elif x[l] <= x[mid]:
        return searchForPivot(x,mid+1,r)

def binarySearchPivot(x, number):
    pivot = searchForPivot(x, 0, len(x) - 1)
    
    if pivot == -1:
        return binarySearch(x, number, 0, len(x) - 1)
    if x[pivot] == number:
        return pivot
    if number < x[0]:
        return binarySearch(x, number, pivot+1, len(x) - 1)
    return binarySearch(x, number, 0, pivot)

