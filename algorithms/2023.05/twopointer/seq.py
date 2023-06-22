def solution(sequence, k):
    answer = [0, len(sequence)]
    s = 0
    index = 0
    for i in range(len(sequence)):
        s += sequence[i]
        while s >= k:
            if s == k:
                if answer[1] - answer[0] > i - index:                  
                    answer = [index, i]
            s -= sequence[index]
            index += 1
            
    return answer