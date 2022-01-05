def solution(m, musicinfos):
    while "#" in m:
        i = m.index("#")
        m = m.replace(m[i-1:i+1], m[i-1].lower(), 1)

    # time
    musicinfoChg = []

    for mi in musicinfos:
        start, end, title, lyrics = mi.split(",")

        hh1, mm1 = int(start.split(":")[0]), int(start.split(":")[1])
        hh2, mm2 = int(end.split(":")[0]), int(end.split(":")[1])

        runningTime = (hh2 * 60 + mm2) - (hh1 * 60 + mm1)

        while "#" in lyrics:
            i = lyrics.index("#")
            lyrics = lyrics.replace(lyrics[i-1:i+1], lyrics[i-1].lower(), 1)

        temp = ""

        for i in range(runningTime):
            temp += lyrics[i % len(lyrics)]
        musicinfoChg.append([temp, title])

    for x in musicinfoChg:
        if m in x[0]:
            return x[1]


print(solution("CC#BCC#BCC#BCC#B", [
    "03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
