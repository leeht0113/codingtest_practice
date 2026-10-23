def solution(price):
    answer = price
    if price >= 100000 and price < 300000:
        answer = answer * 0.95
    elif price >= 300000 and price < 500000:
        answer = answer * 0.9
    elif price >= 500000:
        answer = answer * 0.8 
    return int(answer)