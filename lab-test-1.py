weight = float(input())
if weight <= 5:
    charge = 8
else:
    charge = (weight - 5) * 6
if charge > 60:
    totalCharge = charge + 10
else:
    totalCharge = charge
print(weight)
print(totalCharge)
