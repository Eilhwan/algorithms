import string

# 소수 인지
def isPrime(a):
  if(a<2):
    return 0
  for i in range(2, a ** 0.5):
    if(a%i==0):
      return 0
  return 1
    

# 진법 변환
tmp = string.digits+string.ascii_lowercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

def solution(n, k):
    answer = 0
    if k == 10:
        number = str(n)
    else:
        number = convert(n, k)
    pointer = 0
    for i in range(len(number)):
        if number[i] == "0":
            if number[pointer:i].strip() != "":
                answer += isPrime(int(number[pointer:i]))
                pointer = i + 1
    answer += isPrime(int(number[pointer: len(number)]))
    return answer

print(solution(110011, 10))