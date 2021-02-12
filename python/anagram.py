a = list(input())
b = list(input())

arr_a = [0] * 26
arr_b = [0] * 26

ans = 0

for i in range(len(a)):
    arr_a[ord(a[i]) - ord('a')] += 1
for i in range(len(b)):
    arr_b[ord(b[i]) - ord('a')] += 1



    
            
print(sum(abs(arr_a[i] - arr_b[i])for i in range(len(arr_a)) if arr_a[i] != arr_b[i]))
