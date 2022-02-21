class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["*"] = True

    def search(self, str):
        t = self.trie
        for c in str:
            if c not in t:
                return False
            t = t[c]
        return "*" in t

    def startsWith(self, prefix):
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


t = int(input())
for i in range(t):
    n = int(input())
    answer = "YES"
    trie = Trie()
    phoneNumbers = []
    for _ in range(n):
        phoneNumbers.append(input())

    phoneNumbers.sort(key=lambda x: -len(x))
    for number in phoneNumbers:
        if trie.startsWith(number):
            answer = "NO"
            break
        trie.insert(number)

    print(answer)
