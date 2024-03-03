
def solution(l, x):
    n = len(x)
    bricks = [(x[i], x[i] + l) for i in range(n)]
    bricks.sort()

    heights = {0}  # 초기 높이 0을 포함
    max_height = 0

    for i in range(n):
        new_heights = set()
        for height in heights:
            if bricks[i][0] >= height:
                new_heights.add(height + 1)
        heights.update(new_heights)
        max_height = max(max_height, max(heights))

    result = list(range(1, max_height + 1))
    return result
print(solution(5, [1, 4, 7, 9]))