import math

def solution(picks, minerals):
    answer = 0
    sum =0
    for i in picks:
        sum += i
    # print(sum)
    num = sum * 5
    if len(minerals)>sum:
        minerals = minerals[:num]
    # print(minerals)
    new_minerals =[[0,0,0] for _ in range((math.ceil(len(minerals)/5)))]
    # print(new_minerals)
    for i in range(0, len(minerals), 5):
        temp = minerals[i:i+5]
        new_minerals[i//5][0] = temp.count('diamond')
        new_minerals[i//5][1] = temp.count('iron')
        new_minerals[i//5][2] = temp.count('stone')
    # print(new_minerals)
    new_minerals.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    # print(new_minerals)
    for i in new_minerals:
        dia,iron,stone = i
        for j in range(3):
            if picks[j]>0 and j==0:
                picks[j]-=1
                answer += dia + iron + stone
                break
            elif picks[j]>0 and j==1:
                picks[j]-=1
                answer += (5*dia) + iron + stone
                break
            elif picks[j]>0 and j==2:
                picks[j]-=1
                answer += (25*dia) + (5*iron) + stone
                break
    return answer