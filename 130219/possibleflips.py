def possibleflips(deck):
    moves = []
    for x in range(0, len(deck)):
        if deck[x] != ".":
            if int(deck[x]) == 1:
                moves.append(x)
    return moves
