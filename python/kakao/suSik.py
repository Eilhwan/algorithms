import itertools


def solution(expression):
    answer = []
    operators = ['*', '+', '-']
    per = list(itertools.permutations(operators, 3))
    li = []
    p = 0
    for i in range(len(expression)):
        if expression[i] == '*' or expression[i] == '-' or expression[i] == '+':
            li.append(int(expression[p:i]))
            li.append(expression[i])
            p = i + 1
    li.append(int(expression[p:]))
    for i in range(len(per)):
        s = li.copy()
        p = per[i]
        for j in range(len(p)):
            op = p[j]
            for k in range(len(s)):
                if op == s[k]:
                    operator = s[k]
                    l = 1
                    r = 1
                    while k - l >= 0:
                        if s[k - l] != None and not (s[k - l] == '+' or s[k - l] == '-' or s[k - l] == '*'):
                            operand_left = s[k - l]
                            break
                        l -= 1                   
                    while k + r < len(s):
                        if s[k + r] != None and not (s[k + r] == '+' or s[k + r] == '-' or s[k + r] == '*'):
                            operand_right = s[k + r]
                            break
                        r += 1                       
                    if operator == '+':
                        s[k + r] = operand_left + operand_right
                        s[k] = None
                        s[k - l] = None
                    elif operator == '-':
                        s[k + r] = operand_left - operand_right
                        s[k] = None
                        s[k - l] = None
                    elif operator == '*':
                        s[k + r] = operand_left * operand_right
                        s[k] = None
                        s[k - l] = None
        for c in range(len(s)):
            if s[c] == None:
                s[c] = 0
        answer.append(abs(sum(s)))        
    return max(answer)

print(solution("100-200*300-500+20"))