def solution(s):
    answer = len(s)
    for _ in range(len(s)):
        st = []
        for i in range(len(s)):
            if s[i] == "(" :
                st.append(")")
            elif s[i] == "[" :
                st.append("]")
            elif s[i] == "{":
                st.append("}")
            elif s[i] == ")" or s[i] == "]" or s[i] == "}":
                if st:
                    prev = st.pop()
                    if prev != s[i]:
                        answer -= 1
                        break   
                else:
                    answer -= 1
                    break  
        if st:
            answer -= 1
        s = s[1:] + s[0]
    return answer

print(solution("[](){}"))