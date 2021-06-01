# print(bin(int(input(), 8))[2:])

oct2bin =[
	"000",
	"001",
	"010",
	"011",
	"100",
	"101",
	"110",
	"111"
]

n = input()
s = ""
for i in range(len(n)):
    s += oct2bin[int(n[i])]

p_f = False
for i in range(len(s)):
    if s[i] != "0":
        p_f = True
        print(s[i:])
        break
if not p_f:
    print("0")