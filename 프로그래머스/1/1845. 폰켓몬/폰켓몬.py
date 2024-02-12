def solution(nums):
    phonket = dict()
    for n in nums:
        phonket[n] = phonket.get(n, 0) + 1 
    return min(len(nums)/2, len(phonket.keys()))