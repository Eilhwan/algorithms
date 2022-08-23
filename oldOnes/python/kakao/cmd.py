def solution(n, k, cmd):
    ans = ["O"] * n
    names = [i for i in range(n)]
    st = []

    for i in range(len(cmd)):
        c = list(cmd[i].split())
        if c[0] == "D":
            if k + int(c[1]) < n:
                k += int(c[1])
            else:
                k = n - 1
        elif c[0] == "U":
            if k - int(c[1]) >= 0:
                k -= int(c[1])
            else:
                k = 0       
        elif c[0] == "C":
            st.append(names.pop(k))
            if k  == n - 1:
                k -= 1
            n -= 1
        elif c[0] == "Z":
            temp = st.pop()
            temp_k = names[k]
            for j in range(len(names)):
                if j == len(names) - 1:
                    names.append(temp)
                if names[j] > temp:
                    names.insert(j, temp)
                    break
            for j in range(len(names)):
                if names[j] == temp_k:
                    k = j
                    break
            n += 1

    while st:
        r = st.pop()
        ans[r] = "X"
        
    return "".join(ans)



n = 8	
k = 2	
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]

res = solution(n, k, cmd)

print(res)