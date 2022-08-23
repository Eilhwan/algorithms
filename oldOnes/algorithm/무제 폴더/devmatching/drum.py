
def solution(drum):
    answer = 0
    drumList = []

    for d in drum:
        drumList.append(list(d))

    for i in range(len(drumList[0])):
        isEndRow = False
        starCount = 0
        point = [0, i]
        while True:
            cmd = drumList[point[0]][point[1]]
            if point[0] == len(drumList) - 1:
                isEndRow = True
                break
            if cmd == '#':
                point = [point[0] + 1, point[1]]
            elif cmd == '>':
                point = [point[0], point[1] + 1]
            elif cmd == '<':
                point = [point[0], point[1] - 1]
            elif cmd == '*':
                if starCount == 1:
                    break
                point = [point[0] + 1, point[1]]
                starCount += 1
        if isEndRow:
            answer += 1

    return answer


drum = ["######", ">#*###", "####*#", "#<#>>#", ">#*#*<", "######"]
print(solution(drum))
