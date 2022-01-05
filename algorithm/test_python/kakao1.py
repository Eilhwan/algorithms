def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]

    dic = dict()
    name_dic = dict()

    for id in id_list:
        dic[id] = 0
        name_dic[id] = []

    for r in report:
        repoter, reportee = r.split()
        if reportee not in name_dic[repoter]:
            dic[reportee] += 1
            name_dic[repoter].append(reportee)
    
    for key, val in name_dic.items():
        for v in val:
            if dic[v] >= k:
                answer[id_list.index(key)] += 1

    print(answer)
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]	
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

solution(id_list, report, k)