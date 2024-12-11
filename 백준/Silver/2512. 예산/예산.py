n = int(input())
request = list(map(int, input().split()))
m = int(input())

start = 0
end = max(request)
result = 0
while start <= end:
    mid = (start + end) // 2
    temp = [r if r <= mid else mid for r in request]
    total = sum(temp)
    if total <= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)