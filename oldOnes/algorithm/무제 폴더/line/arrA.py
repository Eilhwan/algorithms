
def solution(arr):
    answer = 0
    li = []
    index = 0
    while index != len(arr):
        for i in range(index, len(arr)):
            if len(arr[index: i+1]) >= 3:
                li.append(arr[index: i+1])
        index += 1

    for e in li:
        peek = e.index(max(e))
        left = peek - 1
        right = peek + 1
        isAList = True
        if peek + 1 == len(e) or peek == 0:
            isAList = False
        if isAList:
            for i in range(peek, len(e) - 1):
                if e[right] >= e[peek]:
                    isAList = False
                peek, right = right, right + 1

            peek = e.index(max(e))
            for i in range(peek, 0, -1):
                if e[left] >= e[peek]:
                    isAList = False
                peek, left = left, left - 1
        if isAList:
            answer += 1
    return answer


arr = [1, 2, 1, 2, 1]
# 부분배열

print(solution(arr))
