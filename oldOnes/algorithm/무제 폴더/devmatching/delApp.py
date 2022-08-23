def solution(n, recipes, orders):
    receipes_dict = dict()

    for s in recipes:
        key, value = s.split()
        receipes_dict[key] = int(value)

    lastOrder = orders[-1].split()

    fires = [1 for _ in range(n)]

    for i in range(len(orders)):
        order = orders[i].split()
        order[1] = int(order[1])
        index = fires.index(min(fires))
        fires[index] = max(fires[index], order[1]) + receipes_dict[order[0]]
        # 정답처리
        if order[1] == int(lastOrder[1]):
            return fires[index]


n = 3
recipes = ["A 10", "B 2"]
orders = ["A 30000"]
# O(n)
print(solution(n, recipes, orders))
