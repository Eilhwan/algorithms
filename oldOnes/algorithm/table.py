def solution(n, k, cmd):
    # "U X" "D X" "C" "Z"
    linked_list = {i: [i - 1, i + 1] for i in range(1, n+1)}
    tab = ["O" for _ in range(1, n + 1)]
    st = []
    k += 1

    for c in cmd:
        if c[0] == "D":
            for _ in range(int(c[2])):
                k = linked_list[k][1]
        elif c[0] == "U":
            for _ in range(int(c[2])):
                k = linked_list[k][0]
        elif c[0] == "C":
            prev, next = linked_list[k]
            st.append([prev, next, k])
            tab[k - 1] = "X"

            if next == n + 1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n + 1:
                linked_list[prev][1] = next
            else:
                linked_list[next][0] = prev
                linked_list[prev][1] = next
        elif c[0] == "Z":
            prev, next, temp = st.pop()
            tab[temp - 1] = "O"

            if prev == 0:
                linked_list[next][0] = temp
            elif next == n + 1:
                linked_list[prev][1] = temp
            else:
                linked_list[prev][1] = temp
                linked_list[next][0] = temp

    return "".join(tab)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
