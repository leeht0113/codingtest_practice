def solution(citations):
    citations.sort()
    for idx, citation in enumerate(citations): # idx->정렬된 배열의 위치, citation->인용수
        # 인용숫자(citation) >= 전체논문 수(len(citations)) - 현재 위치(idx)
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0
    