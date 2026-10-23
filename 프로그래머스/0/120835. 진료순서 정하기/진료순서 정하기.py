def solution(emergency):
    order = []
    for i in sorted(emergency, reverse=True):
        order.append(i)
    return [order.index(x)+1 for x in emergency]