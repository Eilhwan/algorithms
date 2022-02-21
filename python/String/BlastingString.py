

# mirkovC4nizCC44
# C4

s = input()
bomb = input()

st = []

for i in range(len(s)-1, -1, -1):
    c = s[i]
    st.append(c)
    word = st[len(st)-len(bomb):len(st)]
    word.reverse()

    if len(bomb) <= len(st) and "".join(word) == bomb:
        for i in range(len(bomb)):
            st.pop()


if len(st) == 0:
    print("FRULA")
else:
    print("".join(st[::-1]))
