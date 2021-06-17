def solution(orders, course):
    global ans
    ans = []
    dic = {}
    a = []
    for i in range(len(orders)):
        orders[i] = "".join(sorted(list(orders[i])))
    for i in range(len(orders)):
        for j in course:
            for k in range(len(orders[i])):
                recursive(orders[i], "", k, j)
    
    for i in range(len(ans)):
            if ans.count(ans[i]) > 1:
                dic[ans[i]] = ans.count(ans[i])
    for i in course:
        max_val = 0
        for key, value in dic.items():
            if i == len(key):
                max_val = max(value, max_val)
        for key, value in dic.items():
            if i == len(key) and max_val == value:
                a.append(key)
    return a

def recursive(arr, res, index, r):
    global ans
    res += arr[index]
    if r == len(res):
        ans.append(res)
        return
    for i in range(index + 1, len(arr)):
        recursive(arr, res, i, r)
    res = res[:-1]



orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	
course = [2,3,4]

print(solution(orders, course))