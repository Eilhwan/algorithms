from collections import deque


def solution(record):
    st = []
    q = deque()
    fifo = 0
    lifo = 0
    # 선입 선출
    for e in record:
        cmd, price, cnt = e.split()
        price = int(price)
        cnt = int(cnt)
        if cmd == "P":
            q.append([price, cnt])
        else:
            while cnt > 0:
                temp = q.popleft()
                remain = 0
                if cnt >= temp[1]:
                    remain = cnt - temp[1]
                    fifo += temp[1] * temp[0]
                elif cnt < temp[1]:
                    fifo += cnt * temp[0]
                temp[1] -= cnt
                if temp[1] > 0:
                    q.appendleft(temp)
                cnt = remain
    # 후입 선출

    for e in record:
        cmd, price, cnt = e.split()
        price = int(price)
        cnt = int(cnt)
        if cmd == "P":
            st.append([price, cnt])
        else:
            while cnt > 0:
                temp = st.pop()
                remain = 0
                if cnt >= temp[1]:
                    remain = cnt - temp[1]
                    lifo += temp[1] * temp[0]
                elif cnt < temp[1]:
                    lifo += cnt * temp[0]
                temp[1] -= cnt
                if temp[1] > 0:
                    st.append(temp)
                cnt = remain

    return [fifo, lifo]


record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]
print(solution(record))
