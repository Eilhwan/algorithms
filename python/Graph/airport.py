def solution(tickets):
    t = dict()
    for ticket in tickets:
        if ticket[0] in t:
            t[ticket[0]].append(ticket[1])
        else:
            t[ticket[0]] = [ticket[1]]
    for k in t.keys():
        # 알파벳 역순으로 정렬
        t[k].sort(reverse=True)
    print(t)

    st = ["ICN"]
    answer = []

    while st:
        top = st[-1]

        if top not in t or len(t[top]) == 0:
            answer.append(st.pop())
        else:
            st.append(t[top][-1])
            t[top].pop()

        print(st)

    answer.reverse()
    return answer
