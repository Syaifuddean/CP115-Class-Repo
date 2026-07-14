weight = int(input())
ticketPrice = int(input())
if numOfBaggage > 1:
    pass
else:
    finalPrice = ticketPrice - 10.0
if weight <= 15:
    charge = 0
    finalPrice = ticketPrice
else:
    charge = weight - 15 * 4.0
    finalPrice = ticketPrice + charge
print(finalPrice)
