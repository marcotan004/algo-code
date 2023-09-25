def count_inversions(nums, temp_arr, l, r):
    inversions = 0

    if l < r:
        mid = (l + r)//2

        inversions += count_inversions(nums, temp_arr, l, mid)
        inversions += count_inversions(nums, temp_arr, mid + 1, r)

        inversions += merge(nums, temp_arr, l, mid, r)
    
    return inversions

def merge(nums, temp, l, mid, r):
    i = l
    j = mid + 1
    inversions = 0
    k = l

    while i <= mid and j <= r:
        if nums[i] > nums[j]:
            inversions += (mid - i) + 1
            temp[k] = nums[j]
            k += 1
            j += 1
        else:
            temp[k] = nums[i]
            k += 1
            i += 1
    
    while i <= mid:
        temp[k] = nums[i]
        k += 1
        i += 1
    
    while j <= r:
        temp[k] = nums[j]
        k += 1
        j += 1
    
    nums[l:r+1] = temp[l:r+1]

    return inversions


if __name__ == '__main__':
    arr = [2,3,8,6,1]

    print(count_inversions(arr, [0]*5, 0, len(arr)-1))
