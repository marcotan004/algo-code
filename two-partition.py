S = [3, 1, 2, 4, 9, 5]


def twoPartition(S):
    A = sum(S)
    if A % 2 == 1:
        print("2-partition is not possible")
        return False

    k = [[False for i in range(A//2+1)] for j in range(len(S)+1)]
    k[0][0] = -1

    for i in range(1, len(S)+1):
        for j in range(0, A//2+1):
            # case 1
            if k[i-1][j]: 
                k[i][j] = k[i-1][j]
            # case 2
            g = j - S[i-1]
            if g >= 0 and k[i-1][g]:
                k[i][j] = [i-1, g]
    
    i, j = len(S), A//2
    ret, other = [], []

    if not k[i][j]:
        print("2-partition is not possible")
        return False
    
    while k[i][j] != -1:
        if k[i][j] == k[i-1][j]:
            other.append(S[i-1])
            i -= 1
        else:
            ret.append(S[i-1])
            n = k[i][j][0]
            i, j = k[i][j][0], k[i][j][1]
    
    for index in range(0, i):
        other.append(S[index])
    print(f"Original set: {S}\nS1: {ret}\nS2: {other}")

twoPartition(S)


