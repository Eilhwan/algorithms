x, y, w, h = map(int, input().split())

a1 = w - x < x and w - x or x
a2 = h - y < y and h - y or y

print(min(a1, a2))
