from itertools import combinations

def solution(orders, course):
    answer = []
    for order in orders:
        for i in course:
            print(list(combinations(order, i)))
    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	
course = [2,3,4]

solution(orders, course)