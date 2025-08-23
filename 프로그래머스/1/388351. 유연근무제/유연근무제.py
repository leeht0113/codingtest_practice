def solution(schedules, timelogs, startday):
    answer = 0
    for s, time in zip(schedules, timelogs):
        day = startday # 현재 요일
        count = 0 # 늦지 않게 출근한 날
        allow_time = s + 10
        if allow_time % 100 >= 60:
            allow_time += 40
        # print(allow_time)
        for t in time:
            if (day % 7 != 6) and (day % 7 != 0):
                if t <= allow_time:
                    count += 1
            day += 1
        if count == 5:
            answer += 1
    return answer