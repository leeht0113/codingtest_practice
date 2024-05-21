def solution(msg):
    answer = []
    word_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    word_dict = {}
    for idx, w in enumerate(word_list):
        word_dict[w] = idx + 1
    index = 26
    temp = ''
    i = 0
    while i <= len(msg) - 1:
        temp += msg[i]
        # 현재 단어가 사전에 등록되어 있으면
        if word_dict.get(msg[i], 0) != 0:
            # 다음 단어가 사전이 등록될 때까지 탐색
            if len(msg[i + 1:]) > 0:
                for m in msg[i + 1:]:
                    temp += m
                    if word_dict.get(temp,  0) == 0:
                        # 사전에 등록되어 있지 않다면 사전에 등록
                        index += 1
                        word_dict[temp] = index
                        # 이전 단어의 색인 번호 출력
                        answer.append(word_dict[temp[:-1]])
                        i += len(temp[:-1])
                        break
                    # 추가된 단어가 사전에 등록 되어 있다면 answer에 추가
                    else:
                        if i + len(temp) >= len(msg):
                            answer.append(word_dict[temp])
                            return answer
            # 그 다음 단어가 없으면
            else:
                answer.append(word_dict[temp])
                i += 1
        temp = ''
    return answer