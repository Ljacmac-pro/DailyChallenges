pay = int(input("How much did you get paid?"))
tax = 0

cap1 = 12500
cap2 = 45000
cap3 = 15 0000
taxrate1 = 0.25
taxrate2 = 0.4
taxrate3 = 0.45

if pay > cap3:
    tax = tax + ((pay - cap3) * taxrate3)
    pay = cap3

if pay > cap2:
    tax = tax + ((pay - cap2) * taxrate2)
    pay = cap2

if pay > cap1:
    tax = tax + ((pay - cap1) * taxrate1)
    pay = cap1

print("Your tax comes to: "+ str(int(tax)))
