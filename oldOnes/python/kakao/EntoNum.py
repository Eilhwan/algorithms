def solution(s):
    array = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(len(array)):
        s = s.replace(array[i], str(i))
    return s


s = "one4seveneighteight"
print(solution(s))
