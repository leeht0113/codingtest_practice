def solution(genres, plays):
    answer = []
    genre_dict = {}
    for g in range(len(genres)):
        genre_dict[g] = genres[g]
    # print(genre_dict)
    play_dict = {}
    for p in range(len(plays)):
        play_dict[p] = plays[p]
    # print(play_dict)
    most_genre = {}
    for p in play_dict:
        most_genre[genre_dict[p]] = most_genre.get(genre_dict[p], 0) + play_dict[p]
    # print(most_genre)
    # print(sorted(most_genre.items(), reverse=True, key = lambda x: x[1]))
    for m in sorted(most_genre.items(), reverse=True, key = lambda x: x[1]):
        temp = []
        # print(m)
        for g in genre_dict: # 각 곡의 장르
            # print(genre_dict[g])
            if genre_dict[g] == m[0]:
                temp.append([g, play_dict[g]])
        temp = sorted(temp, reverse=True, key = lambda x: x[1])[:2]
        # print(temp)
        for t in temp:
            answer.append(t[0])
    return answer