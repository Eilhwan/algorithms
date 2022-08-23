from itertools import combinations
def solution(relation):
    candidate_key = []
    candidate = []
    for i in range(len(relation[0])):
        relation.sort(key=lambda x: x[i])
        prev = relation[0][i]
        candidate_flag = True
        for j in range(1, len(relation)):
            if prev == relation[j][i]:
                candidate_flag = False
                break
            prev = relation[j][i]
        if candidate_flag:
            candidate_key.append([i])
            candidate.append(i)
    com_keys = []
    for i in range(len(relation[0])):
        if i not in candidate:
            com_keys.append(i)
    keys = []
    for i in range(2, len(com_keys) + 1):
        keys.extend(list(combinations(com_keys, i)))
    for t in range(len(keys)):
        keys[t] = list(keys[t])
    for i in range(len(keys)):
        key_include = False
        for can_key in candidate_key:
            cnt = 0
            for j in can_key:
                if j in keys[i]:
                    cnt += 1
            if cnt == len(can_key):
                key_include = True
                break  
        if not key_include:
            temp = []
            candidate_flag = True
            for j in range(len(relation)):
                temp2 = []
                for k in range(len(keys[i])):
                    temp2.append(relation[j][keys[i][k]])
                temp.append(temp2)
            for j in range(len(temp) - 1):
                for k in range(j + 1, len(temp)):
                    if temp[j] == temp[k]:
                        candidate_flag = False
                        break
                if not candidate_flag:
                    break
            if candidate_flag:
                candidate_key.append(keys[i])
    return len(candidate_key)

# relation = [["100","ryan","music","2", "학생1"],["200","apeach","math","2", "학생2"],["300","tube","computer","3", "학생3"],["400","con","computer","4", "학생4"],["500","muzi","music","3", "학생5"],["600","apeach","music","2","학생6"]]

relation = [[1, 1, 3, 4], [2, 1, 2, 2], [2, 3, 3, 2]]
print(solution(relation))
