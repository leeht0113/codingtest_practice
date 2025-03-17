n = input()
half = len(n)//2
left = n[:half]
right = n[half:]
left_sum = sum([int(l) for l in left])
right_sum = sum([int(r) for r in right])
if left_sum == right_sum:
  print('LUCKY')
else:
  print('READY')