def solution(info, query):
    info_list = []
    for i in info:
        info_list.append(i.split())
    info_list.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4]))

    ans = []
    for q in query:
        temp = q.replace('and', '')
        temp = temp.split()
        same = 0
        for j in info_list:
            is_same = True
            for k in range(len(j)):
                if k != 4 and (j[k] != temp[k]) and temp[k] != "-":
                    is_same = False
                    break
                elif k == 4 and int(j[k]) < int(temp[k]):
                    is_same = False
            if is_same:
                same += 1 
        ans.append(same)

    return ans

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info, query)