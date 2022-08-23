
def to_Knumber(n, k):
    ans = ""
    while n >= 1:
        n, mod = divmod(n, k)
        ans = str(mod) + ans
    return ans


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    number = to_Knumber(n, k)
    num_list = number.split("0")

    for i in num_list:
        if i != "" and int(i) > 1:
            if is_prime(int(i)):
                answer += 1

    return answer
