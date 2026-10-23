def solution(numbers):
    nums=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, num in enumerate(nums):
        numbers = numbers.replace(num,str(idx))
    return int(numbers)