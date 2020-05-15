# aliases
REMOVED, FACE_DOWN, FACE_UP = -1, 0, 1

def flip(state):
    if state == FACE_DOWN:
        return FACE_UP
    elif state == FACE_UP:
        return FACE_DOWN
    elif state == REMOVED:
        return REMOVED

def remove(deck, idx):
    deck[idx] = REMOVED
    if idx > 0:
        deck[idx - 1] = flip(deck[idx - 1])
    if idx < (len(deck) - 1):
        deck[idx + 1] = flip(deck[idx + 1])
    return deck

def simulate(deck, moves):
    if len(moves) < len(deck):
        for idx, i in enumerate(deck):
            if i == REMOVED or i == FACE_DOWN:
                pass
            elif i == FACE_UP:
                moves.append(idx)
                return simulate(remove(deck, idx), moves)
    if 0 in deck:
        return "no solution"
    return moves

if __name__ == '__main__':
    test_data = ['110110101']
    for d in test_data:
        deck = [int(t) for t in d]
        print(simulate(deck, []))
