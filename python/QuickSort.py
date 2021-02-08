

def quick_sort(arr):
    quick_sort_inner(arr, 0, len(arr) - 1)
    return arr

def quick_sort_inner(arr, left, right):
    if left >= right:
        return

    part2 = partition(arr, left, right)
    quick_sort_inner(arr, left, part2 - 1)
    quick_sort_inner(arr, part2, right)

def partition(arr, left, right):
    pivot = arr[int((left + right) / 2)]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while pivot < arr[right]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left

    
arr = [4,2,1,3,6,5,8,7,9,0]
print(quick_sort(arr))