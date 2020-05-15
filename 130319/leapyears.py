year1 = int(input("What is the first year? "))
year2 = int(input("What is the second year? "))

while year1 < 1 or year2 <1 or year2<year1:
    print("Please try again: ")
    year1 = int(input("What is the first year? "))
    year2 = int(input("What is the second year? "))

year1 = year1-1

nnm1 = 0
nnm2 = 0

no1002 = (year2-year2%100)/100
nnn2 = ((no1002-no1002%9)/9) *2
if no1002%9 == 3 or no1002%9 == 7:
    nnm2=1

no1001 = (year1-year1%100)/100
nnn1 = ((no1001-no1001%9)/9) *2
if no1001%9 == 3 or no1001%9 == 7:
    nnm1=1



noleapyears2 = int(((year2-year2%4)/4) - (year2-year2%100)/100) + nnn2 + nnm2
noleapyears1 = int(((year1-year1%4)/4) - (year1-year1%100)/100) + nnn1 + nnm1

print(noleapyears2)
print(noleapyears1)
print(noleapyears2-noleapyears1)
