def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    for i in range(len(seller)):
        temp_seller = seller[i]
        temp_amount = amount[i] * 100
        for j in range(len(enroll)):
            if enroll[j] == temp_seller:
                answer[j] = temp_amount
    
    for i in range(len(referral), -1, -1):
        if answer[i] != 0:
            to_minus = answer[i] / 10
            if to
            answer[i] -= to_minus
            for j in range(len(enroll)):
                if referral[i] == enroll[j]:
                    answer[j] += to_minus
                    break
    return answer