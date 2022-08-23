import sys; read = sys.stdin.readline
from collections import deque



t = int(read().rstrip())

for i in range(t):
    p = read().rstrip()
    while "RR" in p:
        p = p.replace("RR", "")
    p = list(p)

    n = int(read().rstrip())

    s = read().rstrip().lstrip('[').rstrip(']')
    if len(s) > 0:
        d = deque(s.split(','))
    else:
        d = []
    
    flag = False
    for c in p:
        if c == "R":
            flag = not flag
        if c == "D":
            if len(d) == 0:
                break
            if not flag:
                d.popleft()
            else:
                d.pop()
    if d:
        if flag:
            print("[" + ",".join(list(d)[::-1]) + "]")
        else:
            print("[" + ",".join(list(d)) + "]")
    else:
        print("error")
            
        
