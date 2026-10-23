from itertools import combinations

def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1
def solution(nums):
    answer = 0

    total = []
    for t in list(combinations(nums, 3)):
        p = prime_number(sum(t))
        if p == 1:
            answer += 1
    
    return answer