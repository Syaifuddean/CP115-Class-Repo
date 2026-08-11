# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
total_coffee= 3.50 * 2
total_muffin= 2.10* 3
total_water= 1.05* 4
subtotal= total_coffee+total_muffin+total_water
tax= subtotal* 0.06
total= subtotal+tax

print(
    f"==========\tRECEIPT\t==========",
    f"Item\t\t\tPrice\tQty\tTotal",
    f"\nCofee\t\t\t$3.50\t2\t$",total_coffee,"\nMuffin\t\t\t$2.10\t3\t$",total_muffin,"\nwater\t\t\t$1.05\t4\t$total_water",
    f"\n---------------------------------",
    f"\nSubtotal\t\t",subtotal,"\ntax (6%)\t\t",tax,"\nTotal:\t\t\t",total,
  )