def solution(logs):

    students = set()
    studentProblem = dict()

    for l in logs:
        student, num, score = l.split()
        students.add(student)
        studentProblem[student] = [0 for _ in range(101)]

    for l in logs:
        student, num, score = l.split()
        num = int(num)
        studentProblem[student][num] = max(
            studentProblem[student][num], int(score))

    answer = dict()
    for key, value in studentProblem.items():
        temp = []
        for i in range(len(value)):
            if value[i] > 0:
                temp.append([i, value[i]])
        answer[key] = [sum(value), temp]

    res = set()
    for key, value in answer.items():
        for key2, value2 in answer.items():
            if key != key2:
                if value[0] == value2[0] and len(value[1]) == len(value2[1]) and len(value[1]) >= 5:
                    isSame = True
                    for i in range(len(value[1])):
                        if value[1][i][0] != value2[1][i][0] or value[1][i][1] != value2[1][i][1]:
                            isSame = False
                            break
                    if isSame:
                        res.add(key)
                        res.add(key2)

    return list(res).sort()


log = ["1901 10 50", "1909 10 50"]
solution(log)
