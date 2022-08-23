def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    ban = {}

    for r in report:
        reporter, reportee = r.split()
        if reportee not in ban:
            ban[reportee] = []
        if reporter not in ban[reportee]:
            ban[reportee].append(reporter)

    for key in ban.keys():
        if len(ban[key]) >= k:
            for value in ban[key]:
                answer[id_list.index(value)] += 1
    return answer
