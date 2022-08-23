import sys; read = sys.stdin.readline
n = int(read())
nums = list(map(int, read().split()))
money = int(read())
s = ""
cheap = 51
num = 0
for i in range(len(nums) - 1, -1, -1):
    if cheap > nums[i]:
        cheap = nums[i]
        num = i
    
length, pennies = divmod(money, cheap)
for i in range(length):
    pennies += cheap
    index = n - 1
    while index > -1 and pennies > cheap:
        if pennies >= nums[index]:
            pennies -= nums[index]
            s += str(index)
            break
        index -= 1

s += str(num) * (length - len(s))
print(s)




