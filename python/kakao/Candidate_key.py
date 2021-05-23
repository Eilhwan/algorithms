from itertools import combinations

def solution(relation):
    # 단일 컬럼 후보키를 추출한다.    
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
        if candidate_flag:
            candidate_key.append([i])
            candidate.append(i)

    possible_relation = []
    # rel[0].length -> 속성의 개수
    for i in range(len(relation[0])):
        if i not in candidate:
            possible_relation.append(i)

    # 여러 개를 합친 후보키를 찾는다.
    com_relations = []
    if len(possible_relation) > 1:
        for i in range(2, len(possible_relation) + 1):
            temp = list(combinations(possible_relation, i))
            for l in temp:
                com_relations.append(list(l))

    print(candidate_key)
    print(com_relations)
    while com_relations:
        temp = com_relations.pop(0)
        for i in range(len(candidate)):
            for j in range(len(candidate[i])):

    
    return 1
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))


