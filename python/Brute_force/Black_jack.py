n , m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
res = 0
print(cards)
for i in range(n - 2):
    ans = cards[i]
    for j in range(i + 1, n - 1):
        ans += cards[j]
        for k in range(j + 1, n):
            ans += cards[k]
            if ans <= m:
                res = max(ans, res)
            ans -= cards[k]
        ans -= cards[j]
print(res)
