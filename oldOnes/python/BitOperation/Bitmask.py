

relation = [[1, 1, 3, 4], [2, 1, 2, 2], [2, 3, 3, 2]]
answer_list = list()
for i in range(1, 1 << len(relation[0])):
    tmp_set = set()
    for j in range(len(relation)):
        tmp = ''
        for k in range(len(relation[0])):
            if i & (1 << k):
                tmp += str(relation[j][k])
        print(tmp)
        tmp_set.add(tmp)
    print(tmp_set)

    if len(tmp_set) == len(relation):
        not_duplicate = True
        for num in answer_list:
            if (num & i) == num:
                not_duplicate = False
                break
        if not_duplicate:
            answer_list.append(i)
print(answer_list)