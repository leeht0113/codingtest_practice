n = int(input())
card = set(map(int, input().split()))
m = int(input())
card_1 = list(map(int, input().split()))

for c in card_1:
    if c in card:
        print(1, end=' ')
    else:
        print(0, end=' ')