
def solution(str1, str2):
    # 둘 다 케이스 맞추고
    str1 = str1.upper()
    str2 = str2.upper()

    dict1 = {}
    dict2 = {}
    #  두 자씩 나누기
    temp = None
    for i in range(len(str1)):
        if temp is not None and ord("A") <= ord(str1[i]) <= ord("Z") and ord("A") <= ord(temp) <= ord("Z"):
            temp += str1[i]
            if temp not in dict1:
                dict1[temp] = 1
            else:
                dict1[temp] += 1
        temp = str1[i]
    
    temp = None
    for i in range(len(str2)):
        if temp is not None and ord("A") <= ord(str2[i]) <= ord("Z") and ord("A") <= ord(temp) <= ord("Z"):
            temp += str2[i]
            if temp not in dict2:
                dict2[temp] = 1
            else:
                dict2[temp] += 1
        temp = str2[i]
    union = 0
    intersect = 0
    for key, val in dict1.items():
        if key in dict2:
            val2 = dict2[key]
            union += max(val, val2)
            intersect += min(val, val2)
        else:
            union += val
    for key, val in dict2.items():
        if key not in dict1:
            union += val
    if union == 0 or intersect == 0:
        return 65536
    return (int(intersect / union * 65536))

    


    

print(solution("handshake", "shake hands"))