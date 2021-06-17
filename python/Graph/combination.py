# def recursive(arr, res, index, r):
#     global ans
#     res += arr[index]
#     if r == len(res):
#         ans.append(res)
#         return
#     for i in range(index + 1, len(arr)):
#         recursive(arr, res, i, r)
#     res = res[:-1]

# s = "ABCFG"
# ans = []
# for i in range(len(s)):
#     recursive(s, "", i, 2)
# print(ans)

a = ["XYZ", "XWY", "WXA"]
for i in range(len(a)):
    a[i] = "".join(sorted(list(a[i])))
print(a)