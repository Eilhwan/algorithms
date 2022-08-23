def solution(genres, plays):
    answer = []
    songs = dict()
    for i in range(len(genres)):
        if genres[i] not in songs:
            songs[genres[i]] = []
        songs[genres[i]].append([plays[i], i])
    rank = []

    for g, l in songs.items():
        temp = 0
        for i in l:
            temp += i[0]
        rank.append([g, temp])

    rank.sort(reverse=True, key=lambda x: x[1])
    for i in range(len(songs.keys())):
        sorted_list = sorted(songs[rank[i][0]], key=lambda x: (-x[0], x[1]))
        answer.append(sorted_list[0][1])
        if len(sorted(songs[rank[i][0]])) >= 2:
               answer.append(sorted_list[1][1])
    return answer