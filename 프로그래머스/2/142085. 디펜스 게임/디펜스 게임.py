import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    for i, v in enumerate(enemy):
        n -= v
        heapq.heappush(heap, -v)
        # print(heap, n)
        # print('-------------')
        if n < 0:
            if k > 0:
                k -= 1
                prev = -heapq.heappop(heap)
                # print(heap, k)
                n += prev
                answer = i + 1
            else:
                answer = i
                break
        else:
             answer = i + 1
    return answer