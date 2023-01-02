def solution(cap, n, deliveries, pickups):
    answer = 0
    
    index = n - 1 # 목표부터 시작
    remains = sum(deliveries) + sum(pickups)

    while remains > 0:
        d = 0
        p = 0
        f = index
        while True:
            if p + pickups[index] > cap:
                break
            if d + deliveries[index] > cap:
                break
            remains -= (pickups[index] + deliveries[index])
            p += pickups[index]
            d += deliveries[index]
            index -= 1
        
        answer += (f * 2)

    return answer