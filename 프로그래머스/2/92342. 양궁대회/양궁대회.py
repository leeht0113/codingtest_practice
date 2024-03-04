ryan_list = []

def dfs(n, idx, apeach, ryan):
    global answer
    if n == 0:
        ryan_list.append(ryan.copy())
        return
    if idx == 11:
        return
    a_cnt = apeach[idx]
    for i in range(a_cnt + 2):
        if n >= i:
            ryan[idx] = i
            dfs(n - i, idx + 1, apeach, ryan)
            ryan[idx] = 0
            
def calc_score(apeach, ryan):
    a_score = 0
    r_score = 0
    for idx, (a, r) in enumerate(zip(apeach, ryan)):
        if a != 0 or r != 0:
            if a >= r:
                a_score += (10 - idx)
            elif a < r:
                r_score += (10 - idx)
    return a_score, r_score

def solution(n, info):
    global ryan_list
    ryan = [0] * 11
    dfs(n, 0, info, ryan)
    max_score = 0
    answer = []
    for r in ryan_list:
        a_score, r_score = calc_score(info, r)
        if r_score > a_score:
            diff = r_score - a_score
            if diff > max_score:
                max_score = diff
                answer = r
            elif diff == max_score:
                for i in range(11):
                    if r[-i] > answer[-i]:
                        answer = r
                        break
                    elif r[-i] < answer[-i]:
                        break
    if answer:
        return answer
    else:
        return [-1]

# from itertools import combinations_with_replacement
# from collections import Counter

# def solution(n, info):
#     maxdiff, max_comb = 0, {}
    
#     def calculate_score(combi):
#         score1, score2 = 0, 0
#         for i in range(1, 11):
#             if info[10 - i] < combi.count(i):
#                 score1 += i # 라이언
#             elif info[10 - i] > 0:
#                 score2 += i # 어피치
#         return score1, score2
    
#     def calculate_diff(diff, cnt):
#         nonlocal maxdiff, max_comb
#         if diff > maxdiff:
#             max_comb = cnt
#             maxdiff = diff
    
#     for combi in combinations_with_replacement(range(11), n):
#         cnt = Counter(combi)
#         score1, score2 = calculate_score(combi)
#         diff = score1 - score2
#         calculate_diff(diff, cnt)

#     if maxdiff > 0:
#         answer = [0] * 11
#         for n in max_comb:
#             answer[10 - n] = max_comb[n]
#         return answer
#     else:
#         return [-1]