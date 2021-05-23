relation = [[1, 1, 3, 4], [2, 1, 2, 2], [2, 3, 3, 2]]

relation.sort(key=lambda x:x[2])

for i in relation:
    for j in i:
        print(j, end=" ")
    print()