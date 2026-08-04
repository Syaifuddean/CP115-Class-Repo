item_name = input("Enter the name of the item: ")
item_price = float(input("Enter the price of the item: "))
quantity = 3
tax_rate = 0.06
subtotal = item_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Subtotal: RM" + str(subtotal))
print("Tax: RM" + str(tax))
print("Total: RM" + str(total))