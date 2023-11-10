test = [12, 48, 29, 5, 14, 19, 22, 428, 74, 7, 92]

test.sort(reverse=True)

index = 0
for i, num in enumerate(test):
    if num < i:
        break
    index = i+1