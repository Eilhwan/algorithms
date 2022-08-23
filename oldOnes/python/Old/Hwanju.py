
n, k = map(int, input().split())

arr_n = list(range(1, n + 1))
arr_n.sort(reverse=True)
arr_ans = [0 for _ in range(n)]
h_index = n - 1
l_index = 0
for i in range(n):
    if arr_n[i] - 1 <= k:
        k -= arr_n[i] - 1
        arr_ans[l_index] = arr_n[i]
        l_index += 1
    else:
        arr_ans[h_index] = arr_n[i]
        h_index -= 1

for a in arr_ans:
    print(a, end=" ")
