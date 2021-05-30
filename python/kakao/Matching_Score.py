def find_word(word, page):
    count = 0
    word = " " + word.upper() + " "
    head = word[0]
    
    for i in range(len(page)):
        if page[i].upper() == head:
            # 공백을 포함해야할ㄲㅏ?
            if word == page[i: i + len(word)].upper():
                count += 1
        if "<a" == page[i: i+2]:
            start = 0
            end = 0
            for j in range(i, len(page)):
                if page[j] == "\"" and start == 0:
                    start = j + 1
                elif start != 0 and "\"" == page[j]:
                    end = j
                    break
            print(page[start: end])

    return count
            


def solution(word, pages):
    answer = 0
    answer_list = []
    # 기본점수 구하기
    for page in pages:
        answer_list.append(find_word(word, page))
    # for i in range(len(answer_list)):
        
    return answer_list



pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution("Muzi", pages))