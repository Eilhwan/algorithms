import string

tmp = string.digits+string.ascii_uppercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    totalCycle = t * m - (m - t)
    # 진법변환
    nums = ""
    num = 0
    length = 1

    while totalCycle > length:
        temp = str(convert(num, n))

        nums += temp
        length += len(temp)
        num += 1

    # cycle
    answer = []

    for i in range(t):
        answer.append(nums[(m * i) + p - 1])

    return "".join(answer)


n = 16
t = 16
m = 2
p = 1

print(solution(n, t, m, p))
