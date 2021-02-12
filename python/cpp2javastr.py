
a = input().split('_')
ans = ""

if len(a) == 1:
    temp = 0
    for i in range(len(a[0])):
        if ord(a[0][i]) < ord('a'):
            print(a[0][temp: i])
            ans.join(a[0][temp: i] + '_')
            temp = i
else:
    print("".join(a))

print(ans)
print("Error!")