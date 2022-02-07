# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key=lambda x: (x[0], x[1]))
for i in arr:
    print(i[0], i[1])
