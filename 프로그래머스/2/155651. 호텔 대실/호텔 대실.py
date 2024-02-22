def solution(book_time):
    answer = 0
    minutes = []
    for start, end in book_time:
        temp = []
        start_hour, start_minute = start.split(':')
        end_hour, end_minute = end.split(':')
        start_hour = 60 * int(start_hour)
        temp.append(start_hour+int(start_minute))
        end_hour = 60 * int(end_hour)
        temp.append(end_hour+int(end_minute))
        minutes.append(temp)
    minutes.sort(key=lambda x: x[0])
    room = []
    room.append(minutes[0])
    answer += 1
    for m in minutes[1:]:
        if min(room, key=lambda x: x[1])[1]+10 > m[0]:
            room.append(m)
            answer += 1
        else:
            idx = room.index(min(room, key=lambda x: x[1]))
            del room[idx]
            room.append(m)
    return answer