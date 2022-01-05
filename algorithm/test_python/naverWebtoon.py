def recursive(array, index):
    res.append(array)
    print(array, " ")
    # 종료 조건
    # 재귀를 돌리는 부분
    for _ in range(array[index]):
        if index < len(array) - 1:
            array[index] -= 1
            array[index + 1] += 1
            recursive(array, index + 1)


# ATM의 개수 | 입금할 돈 | 연속된 ATM | 제한 돈
def solution(N, money, T, K):
    # 모든 경우의 수를 구해...
    initial = [money] + [0 for _ in range(N - 1)]

    res = recursive(initial, [])

    # 그 중에서 연속된 T개의 ATM에서 K원이 넘는 경우 개수를 빼    
    ans = 0
    for r in res:
        # r = [1, 2, 3, 1]
        for i in range(len(r) - T + 1):
            total = 0
            is_under_K = True
            for j in range(T):
                total += r[i + j]
            if K < total:
                is_under_K = False
                break
        if is_under_K:
            ans += 1

    return ans

res = []
recursive([4, 0, 0], 0)