def rotate_90(arr):
    n = len(arr)
    m = len(arr[0])
    rotated_arr = [[0] * n  for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated_arr[j][n - i - 1] = arr[i][j]
    return rotated_arr

def check(new_lock):
    lock_length = len(new_lock) // 3
    # 3배 이상으로 변경되었기 때문에 정중앙에 lock 배열이 위치함
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    # 자물쇠 리스트의 크기를 3배 이상으로 변경
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    # print(new_lock)
    for _ in range(4):
        key = rotate_90(key)
        for x in range((n * 2)):
            for y in range((n * 2) + 1):
                for i in range(m):
                    for j in range(m):
                        # print((x + i, y + j), (i, j))
                        new_lock[x + i][y + j] += key[i][j]
                # print('----------------')
                if check(new_lock):
                    answer = True
                    return answer
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return answer