
# l은 길이, x는 좌표 왼쪽 위치
def solution(l, x):
    answer = [1, 1]
    l -= 1
    for i in range(2, len(x)):
        max_value = max(answer[i-1], answer[i-2])
        if x[i-1] + l > x[i] > x[i-1] or x[i-1] + l > x[i] + l > x[i-1]:
            answer.append(max_value+1)
        else:
            answer.append(max_value)
    return answer

print(solution(3, [2, 3, 2, 3]))