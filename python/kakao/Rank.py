def solution(info, query):
    answer = []
    res = []
    for i in info:
        i = i.split()
        
        i.extend(i.pop().strip().split())
        answer.append(i)
    print(answer)
    for q in query:
        q = q.split("and")
        cnt = 0
        for i in range(len(info)):
            is_same = True
            for j in range(len(info[i]) - 1):
                if info[i][j] != q[j].strip():
                    is_same = False
                    break
            if is_same and info[i][len(info[i]) - 1] >= 
            if is_same:
                cnt += 1
        res.append(cnt)

    return res


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info, query)