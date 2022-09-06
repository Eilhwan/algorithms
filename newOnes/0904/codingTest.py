def solution(alp, cop, problems):
    time = 0
    objAlp = max(list(map(lambda x: x[0], problems)))
    objCop = max(list(map(lambda x: x[1], problems)))
    
    dpTable = [[] for _ in range(30)]
    dpTable[0] = [alp, cop]
    for i in range(1, len(dpTable)):
        canSolve = list(filter(lambda x: x[0] <= alp and x[1] <= cop, problems))
        dpTable[i].append([dpTable[i-1], dpTable[i-1] + 1])
        dpTable[i].append([dpTable[i-1] + 1, dpTable[i-1]])
        for s in canSolve:
            dpTable[i].append([dpTable[i - s[4]] + s[2], dpTable[i - s[4]] + s[3]])

    return time
    