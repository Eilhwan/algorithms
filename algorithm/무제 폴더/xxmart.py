def solution(id_list, k):
    answer = 0
    client = dict()
    for ids in id_list:
        ids = list(set(ids.split()))
        for i in range(len(ids)):
            if client.get(ids[i]) is None:
                client[ids[i]] = 1
            else:
                client[ids[i]] = client[ids[i]] + 1
    for value in client.values():
        if value > k:
            answer += k
        else:
            answer += value
    return answer


id_list = ["A B C D", "A D", "A B D", "B D"]
k = 2
solution(id_list, k)
