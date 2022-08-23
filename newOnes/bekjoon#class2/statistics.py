
from collections import Counter
import sys

k = int(sys.stdin.readline())

li = []
for _ in range(k):
    li.append(int(sys.stdin.readline()))


# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
print(round(sum(li) / len(li)))
# 둘째 줄에는 중앙값을 출력한다.
print(sorted(li)[len(li)//2])
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
m_v = sorted(list(Counter(li).items()), key=lambda x: (-x[1], x[0]))
if len(m_v) > 1 and m_v[0][1] == m_v[1][1]:
    print(sorted(list(Counter(li).items()), key=lambda x: (-x[1], x[0]))[1][0])
else:
    print(sorted(list(Counter(li).items()), key=lambda x: (-x[1], x[0]))[0][0])
# 넷째 줄에는 범위를 출력한다.
print(max(li) - min(li))