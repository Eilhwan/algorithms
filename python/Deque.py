from collections import deque
import sys


n = int(sys.stdin.readline())
x = deque()

for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "push_front":
        x.appendleft(int(command[1]))
    elif command[0] == "push_back":
        x.append(int(command[1]))
    elif command[0] == "pop_front":
        print(len(x) == 0 and -1 or x.popleft())
    elif command[0] == "pop_back":
        print(len(x) == 0 and -1 or x.pop())
    elif command[0] == "size":
        print(len(x))
    elif command[0] == "empty":
        print(len(x) == 0 and 1 or 0)
    elif command[0] == "front":
        print(len(x) == 0 and -1 or list(x)[0])
    elif command[0] == "back":
        print(len(x) == 0 and -1 or list(x)[len(x) - 1])
