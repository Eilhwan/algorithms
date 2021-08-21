from heapq import heapify, heappush, heappop


def solution(operations):
    answer = []
    is_min_heap = True

    for o in operations:
        instruct, number = o.split()
        if instruct == "I":
            if not is_min_heap:
                number = -int(number)
            else:
                number = int(number)
            heappush(answer, number)
        elif instruct == "D":
            if (number == "-1" and not is_min_heap) or (number == "1" and is_min_heap):
                answer = list(map(lambda x: -x, answer))
                heapify(answer)
                is_min_heap = not is_min_heap
            if answer:
                heappop(answer)
    if answer:
        if is_min_heap:
            return [max(answer), min(answer)]
        else:
            return [min(answer), max(answer)]
    else:
        return [0, 0]

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))