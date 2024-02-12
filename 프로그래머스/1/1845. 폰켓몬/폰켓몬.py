def solution(nums):
    answer = 0
    phonket = dict()
    for n in nums:
        phonket[n] = phonket.get(n, 0) + 1
    answer = min(len(nums)/2, len(phonket.keys()))
    return answer