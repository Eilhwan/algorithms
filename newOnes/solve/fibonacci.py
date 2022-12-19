

dp = [[1, 0], [0, 1]]
index = 2
numbers = []
for i in range(int(input())):
    numbers.append(int(input()))

for j in range(2, max(numbers)+1):
    dp.append([dp[j-1][0] + dp[j-2][0], dp[j-1][1] + dp[j-2][1]])

for i in numbers:
    print(dp[i][0], dp[i][1])


        
