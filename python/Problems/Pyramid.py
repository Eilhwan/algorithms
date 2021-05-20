def solution(enroll, referral, seller, amount):
    sum_amount = dict()
    parents = dict()

    for i in range(len(enroll)):
        sum_amount[enroll[i]] = 0
        parents[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        person = seller[i]
        price = amount[i] * 100
        while price > 0:
            # 위치를 찾고 추천인을 찾고
            temp = parents[person]
            # 돈을 준다.
            if price // 10 < 1:
                sum_amount[person] += price
            else:
                sum_amount[person] += price - (price // 10)
            price = price // 10
            person = temp
            if person == "-":
                break
    
    return list(sum_amount.values())

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))