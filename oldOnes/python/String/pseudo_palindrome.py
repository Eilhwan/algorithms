def is_palindrome(s):
    if s == s[::-1]:
        return True
def palindrome(s):
    if is_palindrome(s):
        return 0
    
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if is_palindrome(s[left + 1 : right + 1]):
                return 1
            elif is_palindrome(s[left: right]):
                return 1
            else:
                return 2
        left += 1
        right -= 1

n = int(input())
ans = []
for _ in range(n):
    s = input()
    ans.append(palindrome(s))

for i in ans:
    print(i)



