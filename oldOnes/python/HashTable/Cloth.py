
def solution(clothes):
    table = dict()
    answer = 1
    for cloth, category in clothes:
        if category not in table:
            table[category] = []
        table[category].append(cloth)
    
    
    
    for i in table.values():
        answer *= (i+1)

    return answer
    


            
    
    