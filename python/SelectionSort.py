
def selection_sort(arr):
    for i in range(len(arr)):
        m = 10e9
        for j in range(i, len(arr)):
            if m > arr[j]:
                m, arr[j] = arr[j], m
        arr[i] = m
    return arr

print(selection_sort([4,2,1,3,6,5]))


    