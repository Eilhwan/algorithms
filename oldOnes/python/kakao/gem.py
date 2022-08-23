

def solution(gems):
    gem_list = dict()
    ans = 100001
    res = [0, 0]
    for gem in gems:
        if not gem in gem_list:
            gem_list[gem] = 0
    p = 0
    for i in range(len(gems)):
        gem = gems[i]
        gem_list[gem] += 1
        val_flag = True
        for val in gem_list.values():
                if val == 0:
                    val_flag = False
                    
        while p < i and val_flag:
            if val_flag:
                if ans > len(gems[p:i + 1]):
                    ans = len(gems[p:i + 1])
                    res = [p + 1, i + 1]
            p += 1
            gem_list[gems[p - 1]] -= 1
            if gem_list[gems[p - 1]] == 0 and gems[p - 1] != gems[p]:
                val_flag = False

    return res

    

gems = ["AA", "AB", "AC", "AA", "AC"]
res = solution(gems)
print(res)