def solution(record):
    answer = []
    ids = {}
    for r in record:
        if r.split()[0] != "Leave":
            action, id, nick = r.split()
            ids[id] = nick
    
    for r in record:
        if r.split()[0] == "Enter":
            action, id, nick = r.split()
            answer.append(ids[id] + "님이 들어왔습니다.")
        elif r.split()[0] == "Leave":
            action, id = r.split()
            answer.append(ids[id] + "님이 나가셨습니다.")
                
    

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])