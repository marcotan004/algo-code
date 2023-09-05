import random

randomList = []
for i in range(10):
    n = random.randint(1,30)
    randomList.append(n)

print(randomList)
randomSet = set(randomList)
inputSet = list(randomSet)  

def calcSize(items, subset, index, target):
    if sum(subset) == target:
        return subset
    
    for i in range(index, len(items)):
        subset.append(items[i])

        if (calcSize(items, subset, i+1, target) != 0):
             return calcSize(items, subset, i+1, target)

        subset.pop();
    
    return 0

print(calcSize(inputSet, [], 0, 43))
