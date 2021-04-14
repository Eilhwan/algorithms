

n, a, b, c, d = map(int, input().split())

div_a, mod_a = divmod(n, a)
div_c, mod_c = divmod(n, c)
if div_a == 0:
    div_a = 1
    
if div_a * b > div_c * d:
    cheap_one = c
    cheap_price = d
    ex_one = a
    ex_price = b
else:
    cheap_one = a
    cheap_price = b
    ex_one = c
    ex_price = d


res = 0

div, mod = divmod(n, cheap_one)
res += div * cheap_price
div, mod = divmod(mod, ex_one)

if mod > 0:
    div += 1

if cheap_price > div * ex_price:
    res += div * ex_price
else:
    res += cheap_price

if ex_one >= n:
    res = min(res, ex_price)

print(res)



