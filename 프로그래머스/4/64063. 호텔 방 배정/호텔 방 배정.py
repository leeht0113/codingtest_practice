import sys
sys.setrecursionlimit(2000)

def solution(k, room_number):
    rooms = dict()
    for num in room_number:
        chk_in = find_emptyroom(num, rooms)
    return list(rooms)

def find_emptyroom(chk, rooms):
    if chk not in rooms: # 할당되지 않은 방이었다면
        rooms[chk] = chk + 1 # 방을 할당하면서 다음 방의 위치를 동시에 기록
        return chk
    empty = find_emptyroom(rooms[chk], rooms) # value는 비어있는 다음 방의 위치
    rooms[chk] = empty + 1 # 빈 방을 찾았으면 다시 할당된 번호로 다음 방의 정보를 기록
    return empty