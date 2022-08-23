def solution(scores):
    answer = ''
    # 학점, 이상, 미만
    grade = [["A", 90], ["B", 80], ["C", 70], ["D", 50], ["F", 0]]
    for j in range(len(scores[0])):
        self_score = 0
        ones_score = []
        for i in range(len(scores)):
            if i == j:
                self_score = scores[i][j]
            ones_score.append(scores[i][j])
        if "".join(map(str, ones_score)).count(str(self_score)) == 1 and (self_score == max(ones_score) or self_score == min(ones_score)):
            temp = (sum(ones_score) - self_score) // (len(scores) - 1)
        else:
            temp = sum(ones_score) // len(scores)
        for i in grade:
            if temp >= i[1]:
                answer += i[0]
                break

            
    return answer

scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

print(solution(scores))