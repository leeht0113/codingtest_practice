def solution(friends, gifts):
    answer = 0
    friends_dict = {f:i for i, f in enumerate(friends)}
    gift_give = [[0] * len(friends) for _ in range(len(friends))]
    gift_get = [[0] * len(friends) for _ in range(len(friends))]
    for g in range(len(gifts)):
        from_, to_ = gifts[g].split(' ')
        gift_give[friends_dict[from_]][friends_dict[to_]] += 1
        gift_get[friends_dict[to_]][friends_dict[from_]] += 1
    total = [[0] * 3 for _ in range(len(friends))]
    for idx, t in enumerate(total):
        # 준 선물
        t[0] = sum(gift_give[idx])
        # 받은 선물
        t[1] = sum(gift_get[idx])
        # 선물 지수
        t[2] = t[0] - t[1]
    for i in range(len(friends)): # 선물을 준 친구
        temp = 0
        for j in range(len(friends)): # 선물을 받은 친구
            # 두 사람이 선물을 주고 받았으면
            if i != j:
                if gift_give[i][j] > 0 or gift_give[j][i] > 0:
                    # 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받음
                    if gift_give[i][j] > gift_give[j][i]:
                        temp += 1
                    # 두 사람이 주고받은 수가 같다면
                    elif gift_give[i][j] == gift_give[j][i]:
                        # 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받음
                        if total[i][2] > total[j][2]:
                            temp += 1
                # 두 사람이 주고받은 기록이 하나도 없다면
                elif (gift_give[i][j] == 0 and gift_give[j][i] == 0):
                    # 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받음
                    if total[i][2] > total[j][2]:
                        temp += 1
        answer = max(answer, temp)
    return answer