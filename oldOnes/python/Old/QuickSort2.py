def quick_sort(arr):
    quick_sort_inner(arr, 0, len(arr) - 1)
    return arr

def quick_sort_inner(arr, left, right):
    if left >= right:
        return

    pi = partition(arr, left, right)

    quick_sort_inner(arr, left, pi - 1)
    quick_sort_inner(arr, pi, right)

def partition(arr, left, right):
    mid = int((left + right) / 2)
    pivot = arr[mid]

    while left <= right:
        while pivot > arr[left]:
            left += 1
        while arr[right] > pivot:
            right -= 1
        
        if right >= left:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left



arr = [4,2,10,1,20,3,6,5,8,7,9,0]
print(quick_sort(arr))