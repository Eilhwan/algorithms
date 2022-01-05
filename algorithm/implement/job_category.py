#   


def solution(table, languages, preference):
    answer = []
    for i in range(len(table)):
        job_nm = table[i].split()[0]
        job = table[i].split()[1:]
        temp = 0
        for j in range(len(languages)):
            if languages[j] in job:
                temp += (5 - job.index(languages[j])) * preference[j]
        answer.append([job_nm, temp])
    print(answer)
    temp = 0
    temp_index = 0
    for i in range(len(answer)):
        if temp < answer[i][1]:
            temp = answer[i][1]
            temp_index = i

        
    return answer[temp_index][0]

table= ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

print(solution(table, languages, preference))