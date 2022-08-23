import re
def solution(registered_list, new_id):
    answer = ''
    r = []
    for i in range(len(registered_list)):
        if "".join(re.findall('[a-z]', new_id)) in registered_list[i]:
            r.append(registered_list[i])
    r.sort()
    
    if new_id not in r:
        return new_id

    S = "".join(re.findall('[a-z]', new_id))

    n = "".join(re.findall('\d', r[0]))    
    if n == "":
        n = "0"

    for i in range(1, len(r)):
        temp = int("".join(re.findall('\d', r[i])))
        if temp - int(n) > 1:
            return S + str(n + 1)
        n = "".join(re.findall('\d', r[i]))
            
    if S + n not in r:
        return S + n
    return S + str(int(n) + 1)

solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow")