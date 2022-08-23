def recursive(arr, index, score):
        global info_dict
        # java -> -
        temp = arr[index]
        arr[index] = "-"
        # -backendjuniorpizza150
        string = "".join(arr)
        if info_dict.get(string) == None:
            info_dict[string] = [score]
        else:
            info_dict[string].append(score)
        for i in range(index + 1, len(arr)):
            recursive(arr, i, score)
        arr[index] = temp

def solution(info, query):
    global info_dict
    info_dict = {}
    res = []
    for i in range(len(info)):
        # java backend junior pizza 150
        temp    = info[i].split()[:-1]
        score   = info[i].split()[4]
        temp_string = "".join(temp)
        if info_dict.get(temp_string) == None:
            info_dict[temp_string] = [score]
        else:
            info_dict[temp_string].append(score)
        for j in range(4):
            recursive(temp, j, score)
        # if info_dict.get("----") == None:
        #     info_dict["----"] = [score]
        # else:
        #     info_dict["----"].append(score)
    
    for q in query:
        temp = q.replace('and', '')
        temp = temp.split()
        string = "".join(temp[:-1])
        score = temp[len(temp) - 1]
        ans = 0
        if info_dict.get(string) is not None:
            for inf in info_dict.get(string):
                if int(score) <= int(inf):
                    ans += 1
        res.append(ans)
    return res


   

    


info =  ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# java  backend junior pizza python backend junior pizza
# -     backend junior pizza
print(solution(info, query))