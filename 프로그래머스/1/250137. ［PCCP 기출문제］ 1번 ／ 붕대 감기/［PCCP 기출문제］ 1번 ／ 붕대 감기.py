from collections import deque

def solution(bandage, health, attacks):
    answer = health
    success = 0
    time, recover, additional = bandage
    attacks = deque(attacks)
    attack_time = attacks[-1][0]
    for i in range(1, attack_time+1):
        # 공격을 안 당하는 경우
        if answer < health and i != attacks[0][0]:
            success += 1
            # print(success)
            # 연속 성공이 시전 시간(time)보다 작은 경우
            if success < time:
                # 최대 체력 이상인 경우
                if answer + recover >= health:
                    answer = health
                else:
                    answer += recover
            # 시전 시간(time) 연속 성공할 경우
            elif success == time:
                success = 0
                # 추가 회복한 체력이 최대 체력보다 작은 경우
                # print(recover, additional)
                if answer + recover + additional < health:
                    answer += (recover + additional)
                    # print(answer)
                # 추가 회복한 체력이 최대 체력보다 클 경우
                else:
                    answer = health
        # 공격을 당하는 경우
        elif i == attacks[0][0]:
            a = attacks.popleft()
            answer -= a[1]
            # print(success)
            success = 0
        if answer <= 0:
            # print(answer)
            return -1
        # print(answer)
    return answer