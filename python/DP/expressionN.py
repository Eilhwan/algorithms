
def solution(N, number):
    oper = ["+", "-", "*", "//"]
    table = [{str(N) * (i + 1)} for i in range(0, 9)]
    for k in range(8):
        temp_list = list(table[k])
        for i in range(len(table[k])):
            for o in oper:
                temp = eval(temp_list[i] + o + str(N))
                if temp == number:
                    return k + 2
                elif temp == 0:
                    continue
                else:
                    table[k + 1].add(str(temp))
    else:
        return -1
    
                


print(solution(5, 12))