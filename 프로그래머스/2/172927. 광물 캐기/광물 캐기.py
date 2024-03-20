import math

def solution(picks, minerals):
    answer = 0
    total = 0
    for p in picks:
        total += p
    num = total * 5
    if len(minerals) > num:
        minerals = minerals[:num]
    minerals_count = [[0, 0, 0] for _ in range(math.ceil(len(minerals)/5))]
    # print(minerals_count)
    # 5개 씩 끊어서 각 광물의 개수를 구함
    for i in range(0, len(minerals), 5):
        temp = minerals[i:i+5]
        minerals_count[i//5][0] = temp.count('diamond')
        minerals_count[i//5][1] = temp.count('iron')
        minerals_count[i//5][2] = temp.count('stone')
    # print(minerals_count)
    # 곡괭이와 광물이 종류가 같으면 최소한의 피로도가 발생
    # 다이아몬드, 철, 돌 곡괭이 순으로 계산되므로 다이아몬드, 철, 돌의 광물 개수를 내림차순으로 처리하는 것이 최소한의 피로도를 보장
    minerals_count.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    # print(minerals_count)
    for i in minerals_count:
        dia, iron, stone = i
        # 각 곡괭이 별로 발생되는 피로도 계산
        for j in range(3):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia + iron + stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (dia*5) + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (dia*25) + (iron * 5) + stone
                break
    return answer