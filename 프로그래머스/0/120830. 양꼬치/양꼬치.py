def solution(n, k):
    yang = n * 12000
    drinks = k * 2000
    answer = yang + drinks
    if n >= 10:
        answer = answer - ((n//10) * 2000) 
    return answer