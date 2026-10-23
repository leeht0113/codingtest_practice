def collatz(num, count):
    if num == 1: 
        return count
    if count == 500:
        return -1
    if num % 2 == 0:
        return collatz(num // 2, count + 1)
    else:
        return collatz(num * 3 + 1, count + 1)

def solution(num):
    return collatz(num, 0)