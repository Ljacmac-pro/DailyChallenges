def scores(input):
    input.sort()
    input.append(0)
    y = 0
    count = 0
    max = 0
    for x in input:
        # print(x,y,count,max)
        count += 1
        if x != y:
            total = count * y
            if total>max:
                max = total
            y = x
            count = 0

    return max

print(scores([1654, 1654, 50995, 30864, 1654, 50995, 22747,
    1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
    30864, 4868, 30864]))
