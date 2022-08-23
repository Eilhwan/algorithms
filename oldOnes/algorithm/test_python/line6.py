from datetime import datetime

def solution(records, k, date):
    answer = []
    date = datetime.strptime(date, "%Y-%m-%d")
    print(date - datetime.strptime(records[i].split()[0].replace('-', ''), "%Y%m%d").day)
    dic = dict()
    # 시간 | 고객 | 상품
    for i in range(len(records) - 1, -1, -1):
        if 0 < date - datetime.strptime(records[i].split()[0], "%y-%m-%d") <= 10:
            record = records[i].split()
            if record[2] in dic:
                if record[1] in dic[record[2]]:
                    print(dic[record[2]][record[1]] + 1)
                    dic[record[2]][record[1]] += 1
            else:
                dic[record[2]] = {record[1]: 1}
    print(dic)
    for key, value in dic.items():
        re_buyer = 0
        buyer = 0
        for k, v in value.items():
            if v > 1:
                re_buyer += 1
            buyer += 1
        re_buy_rate = re_buyer / buyer * 100
        answer.append([key, re_buy_rate])
    print(answer)
    answer.sort(key=lambda x: (x[0], -x[1]))
    answers = []
    for an in answers:
        answers.append(an[0])
    return answers

solution(["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2", "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1", "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3", "2020-03-06 uid1 pid4"], 10, "2020-03-05")