def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    # 배달, 수거 개수
    d, p = 0, 0
    for i in range(n):
        # 물류창고로부터 현재 위치까지 가는 횟수
        cnt = 0
        # 현재 위치의 상자 개수보다 적을 때 까지 택배 상자의 최대 개수를 더하고 방문횟수를 계산 
        while d < deliveries[i] or p < pickups[i]:
            d += cap
            p += cap
            cnt += 1
        # 이전에 더한 택배 상자 수에 현재 위치의 상자 개수를 뺌
        d -= deliveries[i]
        p -= pickups[i]
        # 이동 거리 계산    
        answer += (n - i) * cnt * 2
    return answer