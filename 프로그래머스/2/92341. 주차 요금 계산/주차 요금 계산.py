import math

def solution(fees, records):
    answer = []
    f_time = fees[0]
    fee = fees[1]
    extra_time = fees[2]
    extra_fee = fees[3]
    info_dict = {} # 누적 주차 시간 
    info_in = {} # 마지막 입차 시간
    last_time = 60 * 23 + 59
    for r in records:
        time, car_number, detail = r.split()
        time = list(map(int, time.split(':')))
        time = (60 * time[0]) + (time[1])
        # print(time)
        if detail == 'IN':
            info_in[car_number] = time
            if car_number not in info_dict: # 새롭게 입차된 차량이면 info_dict에 추가
                info_dict[car_number] = 0
            if len(records) == 1:
                info_dict[car_number] = (last_time - list(info_in.values())[0])
                info_in[car_number] = -1 # 출차 처리가 됐으므로 입차 -1로 처리
                break
        else:
            info_dict[car_number] += (time - info_in[car_number])
            info_in[car_number] = -1 # 출차 처리가 됐으므로 입차 -1로 처리
    print(info_dict)
    print(info_in)
    for i in info_in:
        if info_in[i] != -1: # 입차 차량 다음에 출차 차량이 없음
            info_dict[i] += (last_time - info_in[i])
    final_dict = {} # 최종 주차 요금
    car_number = sorted(list(info_dict.keys()))
    for c in car_number:
        if info_dict[c] > f_time:
            # 기본요금 + ((누적주차 시간 - 기본 시간)/단위시간) * 단위 요금
            final_dict[c] = (fee + (math.ceil(((info_dict[c] - f_time)/extra_time)) * extra_fee))
        else:
            final_dict[c] = fee
    return list(final_dict.values())