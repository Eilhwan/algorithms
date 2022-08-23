s = list(input())
arr = [0] * 26
for ch in s:
    arr[ord(ch) - ord('a')] += 1

for i in arr:
    print(i, end=' ')