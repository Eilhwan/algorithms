N = int(input())

sample = []
st = []
st2 = []
ans = []
index = 0
ii = 1

for i in range(N):
    sample.append(int(input()))

while N != len(st2):
    while st and sample[index] == st[-1]:
        a = st.pop()
        st2.append(a)
        ans.append("-")
        index += 1
    if ii <= N:
        st.append(ii)
        ans.append("+")
        ii += 1
    else:
        break

if N == len(st2):
    for i in ans:
        print(i)
else:
    print("NO")
