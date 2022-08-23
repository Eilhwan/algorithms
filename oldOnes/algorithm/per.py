from itertools import permutations
import datetime
a = [1, 2, 3, 4, 5, 6, 7, 8]
start = datetime.datetime.now()
arr = list(permutations(a, 8))

check = [[3, 4], [3, 5], [4, 3], [5, 6], [4, 1]]
answer = 0 
for p in arr:
    for i in check:
        if abs(p.index(i[0]) - p.index(i[1])) == 1:
            answer += 1
            break

print(len(arr) - answer)
print(datetime.datetime.now() - start)


a = 1
b = 2


