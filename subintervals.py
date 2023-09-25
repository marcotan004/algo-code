intervals = [[2.1, 10.3], [4.0, 6.7], [2,5], [1,4.5]]
intervals_2 = [[2,5], [6, 7], [8,9], [10, 23], [12, 15], [16, 24]]
intervals_3 = [[2.1, 10.3], [4.0, 6.7], [2, 5], [4.5, 5.2], [1,15], [10,16]]

sort_list = intervals_2
sort_list.sort(key=lambda x: x[0])

def interval_search(nums,l, r):
    if l > r:
        return []
    elif l == r:
        return [nums[l]]
    
    mid = (l + r)//2

    larray = interval_search(nums, l, mid)
    if larray[-1] == True:
        return larray
    
    rarray = interval_search(nums, mid + 1, r)
    if rarray[-1] == True:
        return rarray
    
    return merge(larray, rarray, l, r)

def merge(larray, rarray, l, r):
    i = 0
    
    if i < len(rarray) and rarray[i][1] <= larray[-1][1]: # extreme value
        return [[larray[-1], rarray[i]], True]
        
    return larray + rarray

interval = interval_search(sort_list, 0, len(sort_list) - 1)

if interval[-1] == True:
    print('{0} is a subinterval of {1}'.format(interval[0][1], interval[0][0]))
else:
    print('There is no such interval')