
def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        temp = arr[i]
        prev = i - 1
        while prev >= 0 and temp < arr[prev]:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = temp
    return arr


print(insertion_sort([4,2,1,3,6,5]))
            