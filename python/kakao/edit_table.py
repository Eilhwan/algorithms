
def solution(n, k, cmd):
    st = []
    pointer = k
    length = n
    table = [i for i in range(n)]
    for c in cmd:
        if c[0] == "U":
            pointer -= int(c[2])
        elif c[0] == "D":
            pointer += int(c[2])
        elif c[0] == "C":
            st.append(table.pop(pointer))
            n -= 1
            if pointer == n:
                pointer -= 1            
        elif c[0] == "Z":
            a = st.pop()
            n += 1
            for i in range(len(table)):
                if table[i] > a:
                    table.insert(i - 1, a)
        if pointer < 0:
            pointer = 0
        elif pointer >= n:
            pointer = n - 1
    ans = ["0" for _ in range(length)]
    for s in st:
        ans[s] = "X"
    return "".join(ans)
            



n = 8
k =	2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

print(solution(n, k, cmd))