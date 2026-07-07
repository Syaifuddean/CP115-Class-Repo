totalKWhConsumed = int(input())
# print(Expression)
if totalKWhConsumed >= 200:
    charges = 0.75
else:
    if totalKWhConsume <= 100:
        charges = 0.3
    else:
        charges = 0.5
totalElectricityBill = totalKWhConsumed + charges
print(totalElectricityBill)
