

s = "one1two2nine3one"
arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for i in range(len(arr)):
    s = s.replace(arr[i], str(i), 1)
print(s)
