N, M = input().split()

# M진법 N을 -> 10진법의 수 X로 변환하라.
# 1234A 11 A -> 10 4 -> 11 * 4
print(int(N, int(M)))

# index = int(len(N))
# ans = 0
# while index:
#     index -= 1
#     target = N[index]
#     if ord("A") <= ord(target) <= ord("Z"):
#         target = ord(target) - ord("A") + 10
#     ans += int(target) * (int(M) ** (len(N) - 1 - index))

# print(ans)
    