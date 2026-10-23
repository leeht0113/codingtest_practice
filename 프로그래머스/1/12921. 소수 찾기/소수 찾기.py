def solution(n):
    # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
    array = [True for _ in range(n + 1)]
    
    # 에라토스테네스의 체 알고리즘 수행
    # 2부터 n의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(n**0.5) + 1):
        if array[i] == True: # i가 소수인 경우
            # i를 제외한 i의 모든 배수를 지우기
            j = 2 # j는 배수 값을 의미함
            while i * j <= n: # i에 j를 곱한 값이 아직 범위를 벗어나지 않았다면 해당 수는 소수가 아니라고 기록함
                array[i * j] = False
                j += 1
    # index 0과 1은 제거
    array = array[2:]
    return array.count(True)