def dfs(start, route):
    
    st = route.get(start)
    while st:
        
        for city in route[start]:
            st.append(city)

def solution(tickets):
    answer = []
    route = {}
    for ticket in tickets:
        if route.get(ticket[0]) == None:
            route[ticket[0]] = []
        route[ticket[0]].append(ticket[1])
    dfs("ICN", route)
    print(route)
    return answer