N = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

answer = [0 for _ in range(N+1)]
answer[1] = -1
st = [1]
while st:
    now = st.pop()

    for i in tree[now]:
        if answer[i] == 0:
            st.append(i)
            answer[i] = now
        
for i in range(2, len(answer)):
    print(answer[i])