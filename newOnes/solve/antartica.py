from itertools import combinations

n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()
if k == 26:
    print(n)
    exit()

alphabets = [False for _ in range(26)]
words = []
answer = 0
for i in range(n):
    word = set(input())
    words.append(word)

for c in ['a', 't', 'c', 'i', 'n']:
    alphabets[ord(c) - ord('a')] = True

def dfs(index, count):
    global answer

    if count == k - 5:
        for i in range(len(alphabets)):
            if alphabets[i]:
                print(chr(i + ord('a')), ', ', end="")
        print()
        tmp_answer = 0
        for i in range(len(words)):
            w = list(words[i])
            for j in range(len(w)):
                _in = True
                if not alphabets[ord(w[j]) - ord('a')]:
                    _in = False
                    break
            if _in:
                tmp_answer += 1
        answer = max(answer, tmp_answer)

    for i in range(index, 26):
        if not alphabets[i]:
            alphabets[i] = True
            dfs(i, count + 1)
            alphabets[i] = False

dfs(0, 0)
print(answer)            

    
