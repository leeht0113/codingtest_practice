def num_divisor(n):
    num = 0
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0) :
            num += 2
            if (n / i == i):
                num -= 1
    return num

def solution(number, limit, power):
    answer = 0
    for n in range(1, number + 1):
        a = num_divisor(n)
        if a > limit:
            answer += power
        else:
            answer += a 
    return answer