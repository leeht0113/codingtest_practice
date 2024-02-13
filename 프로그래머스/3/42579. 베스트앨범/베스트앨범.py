def solution(genres, plays):
    answer = []
    genre_dict = {} # 각 곡 별 장르
    for g in range(len(genres)):
        genre_dict[g] = genres[g]
    # print(genre_dict)
    play_dict = {} # 각 곡 별 재생 횟수
    for p in range(len(plays)):
        play_dict[p] = plays[p]
    # print(play_dict)
    most_genre = {}
    for p in play_dict:
        most_genre[genre_dict[p]] = most_genre.get(genre_dict[p], 0) + play_dict[p]
    # print(most_genre) # 장르별 재생 횟수
    # print(sorted(most_genre.items(), reverse=True, key = lambda x: x[1]))
    for m in sorted(most_genre.items(), reverse=True, key = lambda x: x[1]):
        temp = []
        # print(m)
        for g in genre_dict: # 각 곡 별 장르
            # print(genre_dict[g])
            if genre_dict[g] == m[0]:
                temp.append([g, play_dict[g]])
        # 가장 많이 재생된 장르에 속한 곡의 재생회수 기준으로 정렬
        temp = sorted(temp, reverse=True, key = lambda x: x[1])[:2]
        # print(temp)
        for t in temp:
            answer.append(t[0])
    return answer