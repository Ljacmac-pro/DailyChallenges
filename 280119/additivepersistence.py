import math

number = int(input("What is the number? ")[::-1])
itera = 0

def get_digit(num, n):
    return num // 10**n % 10

while int(math.log10(number))+1 > 1:
    sum = 0
    for i in range(0,int(math.log10(number))+1):
        sum = sum + get_digit(number,i)
    number = sum
    itera = itera + 1

print(itera)
