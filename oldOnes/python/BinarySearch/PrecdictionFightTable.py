def find_n(n):
    res = 0
    while n > 1:
        n = n // 2
        res += 1
    return res


def solution(n, a, b):
    answer = 1
    max_times = find_n(n)
    min_value = 1
    max_value = 8
    while max_times > 1:
        avg = (min_value + max_value) // 2
        if (avg >= a and avg >= b) or (avg < a and avg < b):
            max_times -= 1
            if avg >= a and avg >= b:
                max_value = avg
            else:
                min_value = avg + 1
        else:
            break

    return max_times
