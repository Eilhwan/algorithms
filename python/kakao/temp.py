import re

s = "100-200*300-500+20"
s_list = []
p = 0
for i in range(len(s)):
    if s[i] == '*' or s[i] == '-' or s[i] == '+':
        s_list.append(s[p:i])
        s_list.append(s[i])
        p = i + 1
s_list.append(s[p:])

print(s_list)