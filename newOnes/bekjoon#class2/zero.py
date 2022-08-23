K = int(input())

st = []

for _ in range(K):
    n = int(input())
    if st and n == 0:
        st.pop()
    else:
        st.append(n)
    
print(sum(st))
