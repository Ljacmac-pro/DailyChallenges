import random
inputt = ""


while inputt != "Finish":
    stringg = ""
    inputt = input("What dice? ")
    indexx = inputt.index('d')

    numberof = inputt[0: indexx]

    typeof = inputt[indexx+1: len(inputt)]

    sum = 0

    for i in range(1,int(numberof)):
        roll = random.randint(1,int(typeof))
        sum += roll
        stringg = stringg + str(roll) + " "


    stringg = str(sum)+ ": " + stringg


    print(stringg)
    print("")
