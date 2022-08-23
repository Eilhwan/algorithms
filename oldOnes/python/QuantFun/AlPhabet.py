
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def DFS(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            index = ord(arr[nx][ny]) - ord("A")
            if not visit[index]:
                visit[index] = True
                DFS(nx, ny, cnt + 1)
                visit[index] = False


if __name__ == "__main__":
    ans = 0
    arr = []

    R, C = map(int, input().split())

    for i in range(R):
        arr.append(list(input()))
    visit = [False] * 26  # Alphabet

    visit[ord(arr[0][0]) - ord("A")] = True
    DFS(0, 0, 1)
    print(ans)
