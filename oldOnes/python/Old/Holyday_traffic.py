from datetime import datetime, timedelta

def solution(lines):
    answers = []
    result = []

    for line in lines:
        temp = line.split(' ')
        date = str(temp[0]) + ' ' + str(temp[1])
        if '.' in temp[2]:
            delay = temp[2].split('.')
            delay[1] = delay[1][0: -1]
        else:
            delay = list(temp[2][0: -1])
            delay += '0'
        end = datetime.fromisoformat(date)
        start = end - datetime.timedelta(seconds=int(delay[0], milliseconds=int(delay[1]) - 1))
        result.append([start, end])
    
    for res in result:
        for time in res:
            if compare(time, moment) == True:
                answer += 1
            answers.append(answer)
    return max(answers)

def compare(time, moment):
    # start-end 는 로그의 시작 or 끝 부분부터 시작하는 1초간의 구간.
    start = time
    end = time + datetime.timedelta(milliseconds=999) # => second=1을 인수를 줬을 때, 오류가 생김.
    
    # 1초간의 구간 안에 로그가 겹치는 경우는 3가지 경우만 있음.
    # 1. 구간의 시작보다 로그의 시작이 작고, 구간의 시작보다 로그의 끝이 큰 경우,
    # 2. 구간의 끝보다 로그의 시작이 작고, 구간의 끝보다 로그의 끝이 큰 경우,
    # 3. 구간의 시작보다 로그의 시작이 크고, 구간의 끝보다 로그의 끝이 작은 경우 (구간에 포함 될때)
    if start >= moment[0] and start <= moment[1]:
        return True
    elif end >= moment[0] and end <= moment[1]:
        return True
    elif start <= moment[0] and end >= moment[1]:
        return True
    
    return False
        
