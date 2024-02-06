from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing = deque() # 다리를 건너는 트럭
    end = [] # 다리를 지난 트럭
    truck_weights = deque(truck_weights)
    second = deque([0] * bridge_length) # 다리를 건너는 트럭이 머무는 시간을 담는 배열
    total_trucks = len(truck_weights)
    while len(end) < total_trucks:
        answer += 1
        # 다리를 건너는 트럭이 1개 이상이면 모든 트럭의 머무는 시간을 증가
        ing_length = len(ing)
        if ing_length > 0:
            for i in range(ing_length):
                second[i] += 1
            # 다리를 건너는 첫번째 트럭의 머무는 시간이 bridge_length와 같아지면 제거
            # 제거한 것을 다리를 지난 트럭에 추가
            if second[0] == bridge_length:
                second.popleft()
                second.append(0)
                end.append(ing.popleft())
        # 현재 다리에 있는 truck과 더해질 truck의 수가 bridge_length보다 작고
        # 현재 다리에 있는 truck과 더해질 truck의 무게가 weight보다 작거나 같으면 
        # 다리를 건너는 트럭에 추가
        if len(truck_weights) > 0:
            if len(ing) + 1 <= bridge_length and sum(ing) + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                ing.append(t)
    return answer