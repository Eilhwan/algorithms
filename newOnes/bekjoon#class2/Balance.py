while True:
    s = input()
    if len(s) == 1 and s == '.':
        break
    st = []
    b = True
    for c in s:
        if c in "([":
            st.append(c)
        elif c in ")]":
            if st:
                l = st.pop()
                if c == ")":
                    if l == "[":
                        b = False
                else:
                    if l == "(":
                        b = False
            else:
                b = False
        if not b:
            break            
    if len(st):
        b = False

    print(b and "yes" or "no")
    
