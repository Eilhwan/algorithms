# class Trie:
#     def __init__(self):
#         self.trie = {}

#     def insert(self, word):
#         t = self.trie
#         for c in word:
#             if c not in t:
#                 t[c] = {}
#             t = t[c]
#         t["*"] = True

#     # def search(self, str):
#     #     t = self.trie
#     #     for c in str:
#     #         if c not in t:
#     #             return False
#     #         t = t[c]
#     #     return "*" in t

#     def startsWith(self, prefix):
#         t = self.trie
#         for c in prefix:
#             if c not in t:
#                 return False
#             t = t[c]
#         return True


# t = int(input())
# for i in range(t):
#     n = int(input())
#     answer = "YES"
#     trie = Trie()
#     phoneNumbers = []
#     for _ in range(n):
#         phoneNumbers.append(input())

#     phoneNumbers.sort(key=lambda x: -len(x))
#     for number in phoneNumbers:
#         if trie.startsWith(number):
#             answer = "NO"
#             break
#         trie.insert(number)

#     print(answer)

import sys
input = sys.stdin.readline

for _ in '0'*int(input()):
    ls = [input().rstrip() for _ in '0'*int(input())]
    ls.sort()
    ans = 'YES'
    for p1, p2 in zip(ls, ls[1:]):
        if p2.startswith(p1):
            ans = 'NO'
            break
    print(ans)
