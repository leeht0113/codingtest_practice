def solution(players, callings):
    rank = {key: i for i, key in enumerate(players)}
    for c in callings:
        pre, post = rank[c] - 1, rank[c]
        rank[players[pre]] = post
        rank[players[post]] = pre
        players[pre],  players[post] = players[post], players[pre]
    return players