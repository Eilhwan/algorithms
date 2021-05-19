def solution(absolutes, signs):
    ans = 0
    for i in range(len(absolutes)):
        if signs[i]:
            ans += absolutes[i]
        else:
            ans -= absolutes[i]

    return ans



absolutes = [[4,7,12], [1,2,3]]	
signs = [[True,False,True], [False,False,True]]

for i in range(len (absolutes)):
    print(solution(absolutes[i], signs[i]))