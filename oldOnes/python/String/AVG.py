# 50/70*100이 되어 71.43
n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

ans = 0
for s in scores:
    ans += s / max_score * 100
print(ans / n)