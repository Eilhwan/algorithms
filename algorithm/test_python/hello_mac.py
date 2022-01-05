def solution(student, k):
    seniors = []
    cnt = 0
    for i in range(len(student)):        
        # 재학생 추가
        if student[i] == 1:
            seniors.append(i)
      
        # 신입생 추가
        if len(seniors) == k:
            start = seniors[0]
            end = seniors[-1]
            cnt += 1
            for j in range(start, -1, -1):
                if j == 1:
                    left = start - (j + 1)
                    break
            for j in range(end + 1, len(student)):
                if j == 1 or j == len(student):
                    right = (j - 1) - end
                    break
            cnt += (right * left) + right + left
            seniors.remove(min(seniors))


print(solution([0,1,0,0], 1))