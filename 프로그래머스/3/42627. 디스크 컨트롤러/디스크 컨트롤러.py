from heapq import heappush as push, heappop as pop

def solution(jobs):
    # 현재 시점, 그리고 시작 위치와 처리한 작업의 개수를 기록할 변수 선언
    answer, now, i = 0, 0, 0
    start = -1
    # 우선순위 큐를 담당할 배열
    heap = []
    # 현재 시점에서 처리할 수 있는 모든 작업을 가장 짧은 순서대로 큐에 넣음
    # 현재 시점에서 넣을 수 있는 작업만 큐에 넣고 최소 시간 형태를 유지하도록 만들어야 함
    while i < len(jobs):
        for job in jobs:
            # 요청이 들어온 시점보다 현재 시간이 뒤의 시점이라면 
            # 가장 짧게 걸리는 작업순으로 배치하기 위해 배열을 역순으로 만들어
            # 우선순위 큐에 데이터를 삽입
            if start < job[0] <= now:
                push(heap, job[::-1])
        # print(heap)
        # 작업을 처리하면서 시간을 계속 흘러가게 함
        # 우선순위 큐를 하나씩 비워나가면서 작업을 처리
        if len(heap) > 0:
            cur = pop(heap)
            # print(cur)
            start = now
            # print(start)
            now += cur[0] # 현재 시점에 작업 요청시간을 더함
            answer += now - cur[1] # 현재 시점에서 작업이 요청되는 시점을 뺌
            i += 1 # 현재 검토하는 작업
        else:
            now += 1
            
    return answer // len(jobs)