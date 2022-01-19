def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    d = dict()
    for r in report:
        reporter, reportee = r.split()
        if reportee not in d:
            d[reportee] = []
        if reporter not in d[reportee]:
            d[reportee].append(reporter)

    for key in d.keys():
        if len(d[key]) >= k:
            for c in d[key]:
                answer[id_list.index(c)] += 1



    return answer
