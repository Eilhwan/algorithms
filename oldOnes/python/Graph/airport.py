
def solution(tickets):
    departures = []
    for ticket in tickets:
        departures.append(ticket[0])
        departures.append(ticket[1])

    dic = {e: [] for e in set(departures)}
    visited = {e: [] for e in set(departures)}

    for departure, arrival in tickets:
        dic[departure].append(arrival)
        visited[departure].append(0)

    for ticket in departures:
        dic[ticket] = sorted(dic[ticket])
    print(dic)

    def dfs(cur, res):

        if cur not in dic:
            return res

        for i, val in enumerate(dic[cur]):
            if visited[cur][i] == 0:
                visited[cur][i] = 1
                res.append(val)
                tmp = dfs(val, res)
                if len(tmp) == len(ticket) + 1:
                    return tmp
                visited[cur][i] = 0
                res.pop()
        return res
    answer = dfs("ICN", ["ICN"])
    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
      "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
