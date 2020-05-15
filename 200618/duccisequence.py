def ducci(input, count):
    if all(v == 0 for v in input):
        print(count+1)
        exit()

    start = input[0]

    for i in range(0, len(input)):
        # print(i)
        if i == len(input)-1:
            input[i] = abs(input[i] - start)
        else:
            input[i] = abs(input[i] - input[i+1])

    return ducci(input, count+1)


ducci([0, 653, 1854, 4063],0)
