# def change_notation(num, base):
#     s = ""
#     while num >= base:
#         num, mod = divmod(num, base)
#         s += str(mod)
#     s += str(num)
#     print(s)
#     return s


# n = int(input())
# for i in range(n):
#     num, x = map(int, input().split())
#     changed = change_notation(num, x)
#     if changed == changed[::-1]:
#         print(1)
#     else:
#         print(0)

t = int(input())

for i in range(t):
    A, n = map(int, input().split())
    ans = []
    while True:
        if A == 0:
            break
        x = A % n
        ans.append(x)
        # print(ans)
        A //= n
    flag = True
    for j in range(len(ans)):
        if ans[j] != ans[-1-j]:
            flag = False
    if flag:
        print(1)
    else:
        print(0)