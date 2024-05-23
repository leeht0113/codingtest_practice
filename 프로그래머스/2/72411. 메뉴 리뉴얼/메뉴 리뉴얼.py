from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for o in orders:
            # 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬
            temp += combinations(sorted(o), c)
        max_num = 0
        if len(temp) == 0:
            continue
        for menue in Counter(temp).most_common():
            m, num = menue
            max_num = max(max_num, num)
            if num == max_num and max_num >= 2:
                answer.append(''.join(m))
            else:
                break
    return sorted(answer)