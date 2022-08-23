

# c = int(input())

# arr = []
# avg = []
# for i in range(c):
#     cla = list(map(int, input().split()))[1:]
#     arr.append(cla)
#     avg.append(sum(cla) / len(cla))

# for cla, a in zip(arr, avg):
#     cnt = 0
#     for i in cla:  
#         if i > a:
#             cnt += 1
#     print(f"{cnt / len(cla)*100:0.3f}%")
C = int(input())

for i in range(C):
    score = list(map(int, input().split()))
    cnt = 0
    if score[0] == len(score) - 1:
        aver = (sum(score) - score[0]) / score[0]

    for j in range(1, len(score)):
        if aver < score[j]:
            cnt += 1
    print('%0.3f%%' % ((cnt / score[0]) * 100))