import heapq

def solution(operations):
    answer = []
    heap = []
    for o in operations:
        a, b = o.split()
        b = int(b)
        if a == 'I':
            heapq.heappush(heap, b)
        elif a == 'D':
            if b == -1:
                if len(heap) > 0:
                    heapq.heappop(heap)
            elif b == 1:
                if len(heap) > 0:
                    max_num = max(heap)
                    heap.remove(max_num)
    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), min(heap)]