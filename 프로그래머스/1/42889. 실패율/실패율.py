def solution(N, stages):
    fail_rate = []
    fail = 0
    p = 0 # 스테이지에 도달한 플레이어 수
    f = 0 # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
    for i in range(1, N + 1):
        for j in stages:
            if j >= i:
                p += 1
            if j == i:
                f += 1
        if p == 0:
            fail_rate.append(0)
        else:
            fail_rate.append(f/p)
        f = 0
        p = 0
    number = list(range(1, N + 1))
    a = []
    for x in zip(fail_rate, number):
        a.append(x)
    a.sort(key=lambda x:x[0], reverse=True)
    answer = []
    for i in range(len(a)):
        answer.append(a[i][1])
    return answer