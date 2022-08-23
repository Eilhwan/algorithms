import math
def solution(fees, records):
    
    time_in = dict()
    time_out = dict()
    cars = []
    end_time = 23 * 60 + 59
    for r in records:
        time, number, type = r.split()
        if number not in cars:
            cars.append(number)
        if type == "IN":
            if number not in time_in:
                time_in[number] = []
            time_in[number].append(time)
        else:
            if number not in time_out:
                time_out[number] = []
            time_out[number].append(time)
    cars.sort()
    
    # 요금 계산
    answer = []
    for i in range(len(cars)):
        in_record = time_in[cars[i]]
        if cars[i] in time_out:
            out_record = time_out[cars[i]]
        else:
            out_record = []
        spend_time = 0
        
        for _in, _out in zip(in_record, out_record):
            _in = _in.split(":")
            _out = _out.split(":")
            spend_time += (int(_out[0]) * 60 + int(_out[1])) - (int(_in[0]) * 60 + int(_in[1]))
            
            
        if len(in_record) != len(out_record):
            in_record = in_record[-1].split(":")
            spend_time += end_time - (int(in_record[0]) * 60 + int(in_record[1]))
        
        # fees 기본시간 | 기본 요금 | 단위 시간 | 단위 요금 
        pay = fees[1]
        if fees[0] < spend_time:
            pay += math.ceil((spend_time - fees[0]) / fees[2]) * fees[3]
        answer.append(pay)
    return answer
    # print(time_in)
    # print(time_out)

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))

    