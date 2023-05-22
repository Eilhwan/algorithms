# 5
# 1 1 1 6 0
# 2 7 8 3 1

# N = int(input())

# a = sorted(list(map(int, input().split())))
# b = sorted(list(map(int, input().split())), reverse=True)



# print(sum(map(lambda x, y: x * y, a, b)))

# 입력으로 주어진 배열 A와 B
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A를 B의 순서대로 정렬
sorted_A = [x for _, x in sorted(zip(B, A))]

print(sum(map(lambda x, y: x * y, A, B)))