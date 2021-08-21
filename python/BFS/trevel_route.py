
def solution(tickets):
    departures = []

    for ticket in tickets:
        departures.append(ticket[0])
    dic = {e: [] for e in set(departures)}
    for departure, arrival in tickets:
        dic[departure].append(arrival)
    for ticket in tickets:
        dic[ticket].sort()
    answer = []
    node = "ICN"
    for i in range(len(tickets)):
        answer.append(node)
        node = dic[node].pop()
    print(answer)
    
    

    
            

    

