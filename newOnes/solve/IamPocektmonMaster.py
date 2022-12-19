n, k = map(int, input().split())
po_key_dict = dict()
po_num_dict = dict()
for i in range(n):
    key = input()
    idx = i + 1
    po_key_dict[key] = idx
    po_num_dict[idx] = key


for i in range(k):
    a = input()
    if a.isdigit():
        print(po_num_dict[int(a)])
    else:
        print(po_key_dict[a])