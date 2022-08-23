

arr1    = ["A", "B", "C", "D", "E", "A"]

arr2    = ["A", "Z", "X"]

set1    = set(arr1)

set2    = set(arr2)

set3    = {"A", "B"}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.issuperset(set3))



