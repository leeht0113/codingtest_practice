import math

def solution(arrayA, arrayB):
    answer = 0
    cheolsoo, yeonghee = 0, 0
    for a in arrayA:
        cheolsoo = math.gcd(cheolsoo, a)
    # print(cheolsoo)
    for b in arrayB:
        yeonghee = math.gcd(yeonghee, b)
    # print(yeonghee)
    if cheolsoo != 1:
        for b in arrayB:
            if b % cheolsoo == 0:
                cheolsoo = 0
                break
    else:
        cheolsoo = 0            
    if yeonghee != 1:
        for a in arrayA:
            if a % yeonghee == 0:
                yeonghee = 0
                break
    else:
        yeonghee = 0            
    # print(cheolsoo, yeonghee)
    if cheolsoo == 0 and yeonghee == 0:
        return 0
    else:
        return max(cheolsoo, yeonghee)