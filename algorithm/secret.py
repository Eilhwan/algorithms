def solution(msg):
    answer = {}
    res = []
    INDEX = ord("A")
    for i in range(26):
        answer[chr(INDEX)] = str(INDEX - ord("A") + 1)
        INDEX += 1
    INDEX = INDEX - ord("A") + 1

    prev = 0
    nxt = 1
    while len(msg) >= nxt:
        print(msg[prev:nxt])
        if answer.get(msg[prev:nxt]) == None:
            res.append(int(answer[msg[prev:nxt-1]]))
            answer[msg[prev:nxt]] = str(INDEX)
            prev = nxt - 1
            INDEX += 1
        else:
            nxt += 1

    res.append(int(answer[msg[-1]]))

    print(res)

    return answer


solution("TOBEORNOTTOBEORTOBEORNOT")
