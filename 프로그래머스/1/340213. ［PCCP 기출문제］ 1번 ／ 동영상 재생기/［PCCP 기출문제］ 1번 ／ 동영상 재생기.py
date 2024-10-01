def second(time):
    second = 0
    for idx, v in enumerate(time.split(":")):
        if idx == 0:
            second += int(v) * 60
        else:
            second += int(v)
    return second

def solution(video_len, pos, op_start, op_end, commands):
    video_len = second(video_len)
    answer = second(pos)
    op_start = second(op_start)
    op_end = second(op_end)
    
    for c in commands:
        # 오프닝 구간에 있는 경우 오프닝 끝으로 이동
        if op_start <= answer <= op_end:
            answer = op_end
            
        # 명령어에 따라 이동 처리
        if c == "prev":
            if answer < 10:
                answer = 0  
            else:
                answer -= 10
        elif c == "next":
            if (video_len - answer) < 10:
                answer = video_len
            else:
                answer += 10
        
        # 이동 후에도 오프닝 구간에 있는 경우 처리
        if op_start <= answer <= op_end:
            answer = op_end
    
    return str(answer // 60).zfill(2) + ':' + str(answer % 60).zfill(2)