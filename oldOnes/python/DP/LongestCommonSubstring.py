

A = 'ABCDE'
B = 'BCEDEA'

lcs = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
ans = 0
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            lcs[i][j] += lcs[i - 1][j - 1] + 1
        if ans < lcs[i][j]:
            ans = lcs[i][j]

print(ans)