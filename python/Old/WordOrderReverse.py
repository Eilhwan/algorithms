n = int(input())

for i in range(n):
    arr = list(input().split())
    print(f"Case #{i + 1}:", end=" ")
    for j in range(len(arr) - 1, -1, -1):
        print(arr[j], end=" ")
    print()


