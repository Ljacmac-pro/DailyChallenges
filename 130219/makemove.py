def makemove(deck, i):
    deck[i] = "."
    if i>0 and i<len(deck)-1:
        if deck[i+1] == "0":
            deck[i+1] = "1"
        elif deck[i+1] == "1":
            deck[i+1] = "0"
        if deck[i-1] == "0":
            deck[i-1] = "1"
        elif deck[i-1] == "1":
            deck[i-1] = "0"
    elif i>0:
        if deck[i-1] == "0":
            deck[i-1] = "1"
        elif deck[i-1] == "1":
            deck[i-1] = "0"
    elif i<len(deck)-1:
        if deck[i+1] == "0":
            deck[i+1] = "1"
        elif deck[i+1] == "1":
            deck[i+1] = "0"
    return deck
