def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    # 이진 탐색할 배열 오름차순 정렬
    rocks.sort()
    rocks.append(distance)
    
    # 최소 거리 이진 탐색
    while start <= end:
        # 가장 거리가 짧게 만들 바위 간 거리
        mid = (start + end) // 2
        # 바위 제거 수
        del_stones = 0
        # 이전 바위
        pre_stone = 0
        
        # rocks 배열 돌면서 제거할 바위 개수 세기
        for rock in rocks:
            # 지정한 최소 값보다 작으면 바위 제거
            if rock - pre_stone < mid: del_stones += 1
            # 그렇지 않으면 이전 바위를 현재 바위로 설정
            else: pre_stone = rock
            # 제거할 바위가 직접 지정한 제거할 바위의 수보다 많으면 for loop 종료
            if del_stones > n:
                break
        
        if del_stones > n:
            end = mid - 1

        else:
            answer = mid
            start = mid + 1
            
    return answer