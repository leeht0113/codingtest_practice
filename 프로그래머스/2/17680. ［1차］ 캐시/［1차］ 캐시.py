from collections import deque

def solution(cacheSize, cities):
    answer = 0
    temp = deque()
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for c in cities:
            c = c.lower()
            # 참조리스트에 있으면, 실행시간 1 추가
            if c in temp:
                answer += 1
                temp.remove(c)
            # 참조리스트에 없으면, 실행시간 5 추가
            else:
                answer += 5
                if len(temp) == cacheSize:
                    temp.popleft()
            temp.append(c)
    return answer