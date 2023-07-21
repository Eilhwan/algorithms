from collections import deque

def shortest_path(n, m, maze):
    dx = [-1, 1, 0, 0]  # 상하좌우 x 좌표 변화량
    dy = [0, 0, -1, 1]  # 상하좌우 y 좌표 변화량

    # 방문 여부와 벽 부수기 가능 여부를 저장하는 2차원 리스트
    visited = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1  # 시작점은 방문했다고 표시 (벽 부수기를 사용하지 않음)

    queue = deque([(0, 0, 0)])  # (x, y, 벽 부수기 사용 여부)를 큐에 추가

    while queue:
        x, y, can_break = queue.popleft()

        # 목적지에 도달한 경우 최단 경로를 반환
        if x == n - 1 and y == m - 1:
            return visited[x][y][can_break]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 다음 위치가 범위 내에 있고 아직 방문하지 않았다면 진행
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][can_break] == -1:
                # 벽이 없는 경우
                if maze[nx][ny] == 0:
                    visited[nx][ny][can_break] = visited[x][y][can_break] + 1
                    queue.append((nx, ny, can_break))
                # 벽이 있는 경우 + 벽 부수기를 사용할 수 있는 경우
                elif maze[nx][ny] == 1 and can_break == 0:
                    visited[nx][ny][1] = visited[x][y][can_break] + 1
                    queue.append((nx, ny, 1))

    # 목적지에 도달할 수 없는 경우 -1 반환
    return -1


# 입력 받기
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

# 최단 경로 구하기
result = shortest_path(n, m, maze)

# 결과 출력
print(result)
