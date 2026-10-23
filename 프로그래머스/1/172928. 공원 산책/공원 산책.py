def solution(park, routes):
    rows = len(park)
    columns = len(park[0])

    for i, element in enumerate(park):
        arr = list(element)
        if "S" in arr:
            start = [i, list(arr).index("S")]

    x, y = start
    
    for r in routes:
        
        a, b = r.split(" ")
        b = int(b)
        obstacle = 0
        if a == 'E':
            if y + b > columns-1:
                continue
            else:
                for i in range(1, b+1):
                    if park[x][y+i] == "X":
                        obstacle = 1
                        break
            if obstacle == 1:
                continue
            else:
                y += b
        
        elif a == 'W':
            if y - b < 0:
                continue
            else:
                for i in range(1, b+1):
                    if park[x][y-i] == "X":
                        obstacle = 1
                        break
            if obstacle == 1:
                continue    
            else:
                y -= b
    
        elif a == 'S':
            if x + b > rows - 1:
                continue
            else:
                for i in range(1, b + 1):
                    if park[x+i][y] == "X":
                        obstacle = 1
                        break
            if obstacle == 1:
                continue
            else:
                x += b
                    
        elif a == "N": 
            if x - b < 0:
                continue
            else:
                for i in range(1, b + 1):
                    if park[x-i][y] == "X":
                        obstacle = 1
                        break
            if obstacle == 1:
                continue
            else:
                x -= b
    
    return [x, y]