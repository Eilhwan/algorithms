n = int(input())

arr = list(map(int, input().split()))

mat = [[0 for _ in range(n+1)] for _ in range(n+1)]


for i in range(1, n):
    for j in range(1, n):
        if arr[i] < arr[j]:
            mat[i][j] = max(mat[i-1][j] + 1, mat[i][j-1] + 1)
        else:
            mat[i][j] = 1

print(mat)