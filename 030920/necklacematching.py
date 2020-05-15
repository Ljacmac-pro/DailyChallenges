
string1 = input("")
string2 = input("")



if len(string1) != len(string2):
    print("False")
    exit()

if string1 == "" or string2 == "":
    print("False")
    exit()
 
if string1 == string2:
    print("True")
    exit()

for i in range(1, len(string1)):
    newstring1 = string1[i : len(string1)] + string1[0 : i]
    # print(newstring1)
    if newstring1 == string2:
        print("True")
        exit()


print("False")
