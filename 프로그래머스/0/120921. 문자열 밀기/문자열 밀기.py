from collections import deque

def solution(A, B):
    A, B = deque(A), deque(B)
    for cnt in range(len(A)):
        # A와 B가 같으면 민 횟수를 return
        if A == B:
            return cnt
        # 같지 않으면 rotate
        A.rotate()
    # A를 A의 길이만큼 rotate시켜도 B와 같지 않으면 B가 될 수 없으므로 -1 return
    return -1