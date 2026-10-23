from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)]) # 우선순위를 큐에 넣음
    count = 0 # 요청한 문서의 순서인 location 표시
    priorities.sort(reverse=True) # 우선순위가 높은 순서대로 정렬
    
    while True:
        value, _ = queue[0] # value에 우선순위를 담음
        if value < priorities[count]: # 정렬된 우선순위의 count번째 요소보다 작으면 첫번째 문서가 중요도가 낮은 문서
            queue.append(queue.popleft()) # 꺼내서 가장 마지막에 넣음
        else: # 같으면 인쇄대기 목록이 확정됨
            _, index = queue.popleft() # 인쇄대기 목록의 순서대로 빼감
            count += 1 # 빼갈 때마다 count를 1씩 증가
            if location == index: # 지정된 위치가 첫번째 요소와 같아지면 반복문 종료
                break
    return count