def rock_fe(L, Days):
    minValue = 100 * 1000 / 100
    ans = [0] * 100
    for i in range(len(Days) - L):
        for j in range(len(Days) - i - L + 1):
            temp = Days[i: i + L + j]
            if sum(temp) / (L + j) < minValue:
                minValue = sum(temp) / (L + j)
                ans = temp
            elif sum(temp) / (L + j) == minValue and len(ans) < len(temp):
                minValue = sum(temp) / (L + j)
                ans = temp
            
    return minValue    


print(rock_fe(2, [1,2,3,1,2,3]))