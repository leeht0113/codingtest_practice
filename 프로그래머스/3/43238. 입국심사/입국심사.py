def solution(n, times):
    answer = 0
    # 0분부터 가장 오래 걸리는 소요 시간을 시작과 끝을 지정
    # 가장 오래 걸리는 소요 시간은, 가장 오래 걸리는 심사대에 일렬로 줄을 서는 경우가 됨
    # 전체 인원 수 x 가장 오래 걸리는 시간
    left, right = 1, max(times) * n
    # 시작과 끝의 중간 시간에서 최대 몇 명 심사할 수 있을지 계산
    while left <= right:
        # 탐색할 최대 시간
        mid = (left + right) // 2
        # 주어진 최대 시간 안에 최대로 심사할 수 있는 인원
        people = 0
        test = []
        
        for time in times:
            # 주어진 최대 시간과 심사대의 처리 시간을 나눈 몫을 취해 최대 몇 명을 심사할 수 있는지 확인
            people += mid // time
            # 최대 인원보다 심사 가능한 총 인원이 더 많은 것이 확정되면 더 이상 계산할 필요 없음
            if people >= n:
                break
        
        # 심사해야 할 사람의 숫자보다 많으면 끝의 크기를 줄이고, 적으면 시작의 크기를 줄여 이진 탐색을 수행
        if people >= n:
            # 정답이 될 수 있는 후보는 여유가 남더라도 심사를 받아야 하는 사람보다는 많아야 하기 때문에 정답 변수를 할당
            answer = mid
            right = mid - 1
        
        elif people < n:
            left = mid + 1
                
    return answer