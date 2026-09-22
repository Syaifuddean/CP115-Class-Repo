# Progremmer's Name : Muhammad Syaifuddean Hisham Bin Samasuddin

'''Problem description : PASU Telecommunication Company has made a promotion by giving a discount based on the amount of bill payment every month as in the table below.

You are required to create a Python program that asks the user to enter the monthly usage and then calculates and displays the amount of the bill to be paid after receiving the discount.'''



#PYTHON PROGRAM

#input user monthly_usage
monthly_usage = float(input("Enter your usage : RM ")) 

# monthly usage less than RM50
if monthly_usage < 50 :    
   amount_bill = monthly_usage

# monthly usage less than or equal RM 100
elif monthly_usage <= 100 :        
   amount_bill = monthly_usage + (monthly_usage * 0.05)

#monthly usage more than RM200
else :
   amount_bill = monthly_usage + (monthly_usage * 0.2)

print(f"Amount of the bill to be paid is {amount_bill}")  # Output
 


