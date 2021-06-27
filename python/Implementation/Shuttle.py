def solution(n, t, m, timetable):
    buses = []
    start = "09:00"

    for i in range(n):
        bus = []
        cnt = 0
        for j in range(cnt, len(timetable)):
            cnt += 1
            if m // cnt == 0:
                break
            passenger = timetable[j].replace(":", "")
            if int(start.replace(":", "")) >= int(passenger):
                bus.append(timetable[j])
        buses.append(bus)
        temp = start.split(":")
        temp[1] = int(temp[1]) + t

        if temp[1] >= 60:
            temp[0] = int(temp[0]) + temp[1] // 60
            temp[1] = temp[1] - temp[1] // 60
        
        if int(temp[0]) < 10:
            temp[0] = "0" + str(temp[0])
        else:
            temp[0] = str(temp[0])

        if int(temp[1]) < 10:
            temp[1] = "0" + str(temp[1])
        else:
            temp[1] = str(temp[1])

        start = ":".join(temp)
    print(buses)


            




n = 10
t = 60
m = 45
timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

solution(n, t, m, timetable)