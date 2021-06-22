
def solution(s):
    ans = []
    s = s[1:-1].split('}')
    if s[len(s) - 1] == '':
        s.pop()
    for i in range(len(s)):
        s[i] = s[i].replace('{', '').strip(',').split(',')
    s.sort(key=lambda x: len(x))
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in ans:
                ans.append(s[i][j])
    print(ans)


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"	
solution(s)