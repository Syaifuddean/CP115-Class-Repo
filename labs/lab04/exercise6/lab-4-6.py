minutesBefore = int(input())
membership = (input().lower == 'true')
if membership == True:
    discounts = 0.15
else:
    discounts = 0
concertTicket = 80
if minutesBefore > 30:
    price = 80 - 15
    entry = True
    print(entry)
else:
    if minutesBefore <= 0:
        price = 0
        entry = False
    else:
        price = 80
        entry = True
    print(entry)
print(price)
