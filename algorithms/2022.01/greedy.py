
T = int(input())
# 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)
coins = [25, 10, 5, 1]
for _ in range(T):
    c = int(input())
    ans = [0, 0, 0, 0]
    for i in range(len(coins)):
        div, mod = divmod(c, coins[i])
        if mod == 0:
            break
        ans[i] = div
        c = mod
    print(" ".join(map(str, ans))[:-2])
        