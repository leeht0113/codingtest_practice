from collections import deque

def check(deck1, deck2, target):
    operand = set(deck2)
    for card in deck1:
        if target - card in operand:
            deck1.remove(card)
            deck2.remove(target-card)
            return True
    return False

def solution(coin, cards):
    hand = cards[:len(cards)//3]
    deck = deque(cards[len(cards) // 3:])
    pending = []
    answer = 1
    while coin >= 0 and deck:
        pending.append(deck.popleft())
        pending.append(deck.popleft())
        # 코인을 사용하지 않고 손에 든 카드로만 턴을 넘길 경우
        if check(hand, hand, len(cards) + 1):
            pass
        # 코인 1개를 사용하고 손에 든 카드 1장, 뽑은 카드 1장으로 턴을 넘길 경우
        elif coin >= 1 and check(hand, pending, len(cards) + 1):
            coin -= 1
        # 코인 2개를 사용하고, 뽑은 카드로만 턴을 넘길 경우
        elif coin >= 2 and check(pending, pending, len(cards) + 1):
            coin -= 2
        else:
            break
        answer += 1
    return answer