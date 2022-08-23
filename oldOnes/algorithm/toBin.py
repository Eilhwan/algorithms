def solution(s):

    countZero = 0
    convertCount = 0
    while s != "1":
        num = s.count('1')
        countZero += len(s) - num
        convertCount += 1

        s = bin(num)[2:]

    return [convertCount, countZero]


solution("110010101001")
