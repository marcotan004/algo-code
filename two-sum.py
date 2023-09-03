import random

randomList = []
for i in range(10):
    n = random.randint(1,30)
    randomList.append(n)

randomSet = set(randomList)
inputSet = list(randomSet)

def twoSum(theSet, target):
    theSet.sort()

    leftPoint = 0
    rightPoint = len(theSet) - 1

    while (theSet[leftPoint] + theSet[rightPoint]) != target and leftPoint <= rightPoint:
        if (theSet[leftPoint] + theSet[rightPoint]) > target:
            rightPoint -= 1
        else:
            leftPoint += 1
    
    if (theSet[leftPoint] + theSet[rightPoint]) == target:
        return True
    
    return False
 
print(twoSum(inputSet, 12))