import sys
input = sys.stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum = 0
for i in range(k):
    prefix_sum += nums[i]

max_sum = prefix_sum
for i in range(k, n):
    prefix_sum += nums[i]
    prefix_sum -= nums[i - k]
    max_sum = max(max_sum, prefix_sum)

print(max_sum)