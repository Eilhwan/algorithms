# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
def is_prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


M, N = map(int, input().split())

for i in range(M, N+1):
    if is_prime(i) and i != 1:
        print(i)
