K = 14
n = [25, 20, 10, 12, 5] # []
nf = [[25, 10], [25, 12], [10, 20], [10, 15], [5, 4]]
def knapsackProblem(n, K):
    knapsack = [[False for i in range(K+1)] for j in range(len(n)+1)]
    
    # case 1 - knapsack [i-1, K] = true --> knapsack[i, K] = true
    # case 2 - knapsack [i-1, K - n[i]] = true --> knapsack[i, K] = true
    
    # initialize 0 to true
    knapsack[0][0] = True
    
    for i in range(1, len(n)+1):
        for j in range(0, K+1):
            # case 1
            if knapsack[i-1][j]: 
                knapsack[i][j] = True
            # case 2
            g = j - n[i-1]
            if g >= 0 and knapsack[i-1][g]:
                knapsack[i][j] = True
    
    return knapsack[len(n)][K]

def betterSpace(n, K):
    recent = [False for i in range(K+1)]
    next = [False for i in range(K+1)]

    recent[0] = True

    for i in range(1, len(n)+1):
        for j in range(0, K+1):
            # case 1
            if recent[j]: 
                next[j] = True
            # case 2
            g = j - n[i-1]
            if g >= 0 and recent[g]:
                next[j] = True
            
        recent = next
        next = [False for i in range(K+1)]
    
    return recent[-1]

def valueKnapsack(n, K):
    knapsack = [[False for i in range(K+1)] for j in range(len(n)+1)]
    values = [[float('-inf') for i in range(K+1)] for j in range(len(n)+1)]
    parent = [[False for i in range(K+1)] for j in range(len(n)+1)]
    # case 1 - knapsack [i-1, K] = true --> knapsack[i, K] = true, value[i, K] = value[i-1, K], parent[i, K] = parent(i-1, K)
    # case 2 - knapsack [i-1, K - n[i]] = true --> knapsack[i, K] = true, value[i, K] = max(value[i, K], value[i-1, g])
    
    # initialize 0 to true
    knapsack[0][0] = True
    values[0][0] = True
    parent[0][0] = -1

    for i in range(1, len(n)+1):
        for j in range(0, K+1):
            # case 1
            if knapsack[i-1][j]: 
                knapsack[i][j] = True
                values[i][j] = values[i-1][j]
                parent[i][j] = parent[i-1][j]
            # case 2
            g = j - n[i-1][0]

            if g >= 0 and knapsack[i-1][g]:
                knapsack[i][j] = True
                if values[i-1][g] + n[i-1][1] > values[i-1][j]:
                    values[i][j] = values[i-1][g] + n[i-1][1]
                    parent[i][j] = [i-1, g]

    if not knapsack[len(n)][K]:
        print("No subset exists")
        return
    
    ret = []
    total = 0
    i = len(n)
    j = K
    while parent[i][j] != -1:
        if parent[i][j] == parent[i-1][j]:
            i -= 1
        else:
            ret.append(n[i-1])
            total += n[i-1][1]
            i, j = parent[i][j][0], parent[i][j][1]

    print(f"Knapsack found with total value {total} and items {ret}")

print(knapsackProblem(n, K))
print(betterSpace(n, K))
valueKnapsack(nf, K)
