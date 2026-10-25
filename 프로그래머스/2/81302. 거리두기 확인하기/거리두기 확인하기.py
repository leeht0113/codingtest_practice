def check(place):
    for row_idx, row in enumerate(place):
        for col_idx, column in enumerate(row):
            next_row = row_idx + 1
            next_col = col_idx + 1
            prev_col = col_idx - 1
            if column == "P":
                # 거리 1인 경우
                if next_row < 5 and place[next_row][col_idx] == "P":
                    return 0
                if next_col < 5 and place[row_idx][next_col] == "P":
                    return 0
                if (next_row < 5 and next_col < 5) and (place[next_row][col_idx] != "X" or place[row_idx][next_col] != "X"):
                    if place[next_row][next_col] == "P":
                        return 0
                if next_row < 5 and prev_col >= 0:
                    if place[next_row][col_idx] != "X" or place[row_idx][prev_col] != "X":
                        if place[next_row][prev_col] =="P":
                            return 0
                # 거리 2인 경우
                if next_col < 5 and next_col + 1 < 5 and place[row_idx][next_col] != "X": 
                    if place[row_idx][next_col + 1] == "P":
                        return 0
                if next_row < 5 and next_row + 1 < 5 and place[next_row][col_idx] != "X":
                    if place[next_row + 1][col_idx] == "P":
                        return 0
    return 1    
def solution(places):
    return [check(place) for place in places]