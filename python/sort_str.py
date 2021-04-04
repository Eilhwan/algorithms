

n = int(input())
table = set()
for i in range(n):
    table.add(input())
table_list = list(table)
table_list.sort(key= lambda x: (len(x), x))

for string in table_list:
    print(string)