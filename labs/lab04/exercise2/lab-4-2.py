income = int(input())
if income <= 50000:
    if first:
        incomeTax = 0.0
    else:
        incomeTax = 0.01
else:
    incomeTax = 0.02
totalTax = income * incomeTax
print(totalTax)
