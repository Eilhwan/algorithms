from collections import Counter

def solution(weights, head2head):
    answer = []
    # 전체 승률 순
    for i in range(len(weights)):
        if "W" in head2head[i]:
            wln = dict(Counter(head2head[i]))
            temp = str(wln["W"] / ((len(head2head[i]) - 1) - wln["N"]) * 100)
            answer.append([i, float(temp[:temp.index('.') + 3])])
        else:
            answer.append([i, 0])
    answer.sort(key=lambda x : -x[1])

    # 자신보다 몸무게를 높은 복서를 이깃 횟수
    for i in range(1, len(answer)):
        if answer[i][1] == answer[i - 1][1]:
            num1 = answer[i][0]
            num2 = answer[i - 1][0]
            cnt = 0
            cnt2 = 0
            for j in range(len(head2head[num1])):
               if head2head[num1][j] == "W" and weights[j] > weights[num1]:
                   cnt += 1
            for j in range(len(head2head[num2])):
               if head2head[num2][j] == "W" and weights[j] > weights[num2]:
                   cnt2 += 1
            if cnt > cnt2:
                answer[i], answer[i - 1] = answer[i - 1], answer[i]
            elif cnt == cnt2:
                if weights[num1] > weights[num2]:
                    answer[i], answer[i - 1] = answer[i - 1], answer[i]
                elif weights[num1] == weights[num2]:
                    if num2 > num1:
                        answer[i], answer[i - 1] = answer[i - 1], answer[i]
    # 몸무게
    res = [answer[i][0] + 1 for i in range(len(answer))]
    # 번호
    return res

weight = [50,82,75,120]	
head2head = ["NLWL","WNLL","LWNW","WWLN"]	

print(solution(weight, head2head))
# result [3,4,1,2]

# None Win Lose
