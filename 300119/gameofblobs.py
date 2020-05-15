import numpy as np

def initialisetable(input):
    xmax = 0
    ymax = 0
    for i in input:
        if i[0] > xmax:
            xmax = i[0]
        if i[1] > ymax:
            ymax = i[1]
    table = [ [0] * (ymax+1) for _ in range((xmax+1))]
    for i in input:
        table[i[0]][i[1]] = i[2] + table[i[0]][i[1]]
    return table

def boardblobs(table):
    min = 0
    max = 0
    list = []
    # print(table)
    for i in range(0,len(table)):
        k = table[i]
        for j in range(0,len(k)):
            if k[j] != 0:
                if list == []:
                    # print("Got here")
                    min = k[j]
                    max = k[j]
                else:
                    if k[j] < min:
                        min = k[j]
                    if k[j] > max:
                        max = k[j]
                list.append([i,j,k[j]])
    return list, min, max

def makechoice(oldstates, newstates, blobinq):
    bestdistance = 1000
    bestblob = 0
    choice = []
    for i in oldstates:
        # print(i)
        if i[2] < blobinq[2]:
            diffx = (i[0]-blobinq[0])
            diffy = (i[1]-blobinq[1])
            distance = abs(diffx)+abs(diffy)
            if i[2] > bestblob:
                bestblob = i[2]
                if distance < bestdistance:
                    choice = [i,diffx,diffy]
                elif distance == bestdistance:
                    print("Whhops")


    if choice != []:
        if blobinq[0] - choice[0][0] >0:
            changex = -1
        elif blobinq[0] - choice[0][0] < 0:
            changex = 1
        else:
            changex = 0
        if blobinq[1] - choice[0][1] >0:
            changey = -1
        elif blobinq[1] - choice[0][1] < 0:
            changey = 1
        else:
            changey = 0
        newstates.append([blobinq[0]+changex,blobinq[1]+changey,blobinq[2]])
    else:
        newstates.append(blobinq)


    return newstates

def disp(table):
    lines = []
    for row in table:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))


def gameofblobs(input):
    table = initialisetable(input)
    disp(table)
    print("")
    blobstates, min, max = boardblobs(table)
    while min != max:
        newstates = []
        for i in blobstates:
            # print(i)
            newstates = makechoice(blobstates, newstates, i)
            # print(newstates)
        newtable = initialisetable(newstates)
        disp(newtable)
        print("")
        blobstates, min, max = boardblobs(newtable)
    return blobstates

print(gameofblobs([(4, 3, 4),
 (4, 6, 2),
 (8, 3, 2),
 (2, 1, 3)]))
