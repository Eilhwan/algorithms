import re

s = "123abc."

s = s.lower()
s = re.sub('[^a-z0-9\-_.]', '', s)
s = re.sub('\.+', '.', s)
s = re.sub('^[.]|[.]$', '', s)
s = 'a' if len(s) == 0 else s[:15]
s = re.sub('^[.]|[.]$', '', s)
s = s if len(s) > 2 else s + "".join([s[-1] for i in range(3-len(s))])

print(s)

