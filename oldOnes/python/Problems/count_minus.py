s1 = '12:05:45AM'
s2 = '01:05:45PM'

if s1[-2:] == "AM":
    h = s1[:2]
    if int(h) == 12:
        h = "00"
else:
    h = s1[:2]
    if int(h) > 12:
        h = str(int(h) + 12)

print(h + s1[2:-2])


