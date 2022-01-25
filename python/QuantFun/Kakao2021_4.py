max_value = 0
res = []


def solution(n, info):
    global res, max_value
    ryan = [0 for _ in range(len(info))]

    def dfs(info, cnt, index):
        global res, max_value

        if cnt == index + 1:
            apeech_point = 0
            ryan_point = 0
            for i in range(11):
                if info[i] != 0 or ryan[i] != 0:
                    if info[i] < ryan[i]:
                        ryan_point += 10 - i
                    else:
                        apeech_point += 10 - i
            if ryan_point > apeech_point and (ryan_point - apeech_point) > max_value:
                res = ryan.copy()
                max_value = ryan_point - apeech_point

            return
        for i in range(11):
            ryan[i] += 1
            dfs(info, cnt + 1, index)
            ryan[i] -= 1

    dfs(info, 1, n)

    return res


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
