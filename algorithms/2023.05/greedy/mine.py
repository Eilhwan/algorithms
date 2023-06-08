def solution(picks, minerals):
    answer = 0
    stones = [0, 0, 0]
    for mineral in minerals:
        if mineral == "diamond":
            stones[0] += 1
        elif mineral == "stone":
            stones[1] += 1
        else:
            stones[2] += 1
    picks = list(map(lambda x: x * 5, picks))
    index = 0
    for i in range(len(stones)):
        s = stones[i]
        while picks[index] > 0:
            s - picks[index]

    print(minerals)
    
    return answer