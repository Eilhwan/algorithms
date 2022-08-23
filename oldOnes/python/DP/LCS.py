
# A = input()
# B = input()

# lcs = [[0 for _ in range(len(B) + 1)]for _ in range(len(A) + 1)]

# for i in range(1, len(A) + 1):
#     for j in range(1, len(B) + 1):
#         if A[i - 1] == B[j - 1]:
#             lcs[i][j] = lcs[i - 1][j - 1] + 1
#         else:
#             lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

# print(max(max(lcs)))
def s():
    s1, s2 = input(), input()
    dp = [0] * 1000
    for i in range(len(s1)):
        s = ""
        max_dp = 0
        for j in range(len(s2)):
            if max_dp < dp[j]:
                max_dp = dp[j]
            elif s1[i] == s2[j]:
                s += s1[i]
                dp[j] = max_dp + 1
    print(max(dp))
    print(s)


s()
