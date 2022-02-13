

N, M = map(int, input().split())

res = []
arr = [-1 for _ in range(N+1)]
state = [0 for _ in range(N+1)]


def recursive(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=" ")
        print()
        return

    for i in range(1, N+1):
        if state[i] == 0:
            arr[k] = i
            state[i] = 1
            recursive(k+1)
            state[i] = 0


if "__main__" == __name__:
    recursive(0)
