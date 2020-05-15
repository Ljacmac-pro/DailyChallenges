def recursivejob(input):
    if input == 16:
        print("This worked")
        exit()
    for i in input:
        print("gOTHERE")

        return recursivejob(i)



recursivejob([[12],[13],[13],[16]])
