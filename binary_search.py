import random

x=[random.randint(0,10) for i in range(25)]
x.sort()

def binary_search(x, search, low, high):
    if high < low:
        return -1
    
    r = (high + low) // 2

    if search == x[r]:
        return r
    
    if search < x[r]:
        return binary_search(x, search, low, r-1)
    else:
        return binary_search(x, search, r+1, high)

print(binary_search(x, 4, 0, len(x)))
print(x)