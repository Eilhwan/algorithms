
def solution(fees, records):
    answer = []
    res = []
    cars = dict()

    for record in records:
        time, number, io = record.split()

        if cars.get(number) is None:
            cars[number] = []
        cars[number].append([time, io])

    for key in cars.keys():
        time = 0
        temp = 0
        for r in cars[key]:
            t, m = r[0].split(":")
            if r[1] == "IN":
                time = int(t) * 60 + int(m)
            else:
                temp += (int(t) * 60 + int(m)) - time

        if r[1] == "IN":
            last = 23 * 60 + 59
            temp += last - time
        answer.append(temp)

    for a in answer:
        temp = fees[1]
        f = 0
        if a > fees[0]:
            left = a - fees[0]
            f = (left // fees[2]) * fees[3]

        res.append(temp + f)

    return res


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(fees, records)
