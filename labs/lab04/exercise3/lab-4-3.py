hours = int(input())
if hours <= 2:
    unitPrice = 0
    parkingFee = 0
else:
    if hours <= 5:
        unitPrice = 2.0
        parkingFee = hours - 2 * 2.0
    else:
        unitPrice = 3.0
        parkingFee = hours - 2 * 3.0
if unitPrice <= 30:
    print(parkingFee)
else:
    print("You have maximum charge for this day")
