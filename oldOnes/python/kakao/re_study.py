import re

# data = """
# park 800905-1049118
# kim  700905-1059119
# """

# result = []
# for line in data.split("\n"):
#     word_result = []
#     for word in line.split(" "):
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#             word = word[:6] + "-" + "*******"
#         word_result.append(word)
#     result.append(" ".join(word_result))
# print("\n".join(result))

# # s = "123abc."

# # s = s.lower()
# # s = re.sub('[^a-z0-9\-_.]', '', s)
# # s = re.sub('\.+', '.', s)
# # s = re.sub('^[.]|[.]$', '', s)
# # s = 'a' if len(s) == 0 else s[:15]
# # s = re.sub('^[.]|[.]$', '', s)
# # s = s if len(s) > 2 else s + "".join([s[-1] for i in range(3-len(s))])

# # print(s)

a = "12345"
print(str(re.match('[\d]', a)))