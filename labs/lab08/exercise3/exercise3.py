day_type = input()
show_time = int(input())
customer_type = input()

if day_type == "weekend" and show_time > 18 and customer_type == "Adult" :
    base_price = 18 
    final_price = 18 +3
elif day_type == "weekend" and show_time > 18 and customer_type ==" Child" :
    base_price = 12 
    final_price = 12+3
elif day_type == "weekend" and show_time > 18 and customer_type =="Senior" :
    base_price = 15 
    final_price = 15+3
elif day_type == "weekday" and show_time > 18 and customer_type == "Adult" :
    base_price = 15 
    final_price = 15+3
elif day_type == "weekday" and show_time > 18 and customer_type == " Child" :
    base_price = 10
    final_price = 10+3 
elif day_type == "weekday" and show_time > 18 and customer_type =="Senior" :
    base_price = 12 
    final_price = 12+3
elif day_type== "weekend" and show_time <18 and customer_type =="Adult" :
    base_price = 18
    final_price = 18
elif day_type == "weekend" and show_time <18 and customer_type ==" Child" :
    base_price = 12
    final_price = 12
elif day_type == "weekend" and show_time <18 and customer_type =="Senior" :
    base_price = 15
    final_price = 15
elif day_type== "weekday" and show_time <18 and customer_type =="Adult" :
    base_price = 15
    final_price = 15
elif day_type == "weekday" and show_time <18 and customer_type ==" Child" :
    base_price = 10
    final_price = 10
else :
    base_price = 12
    final_price = 12








print(base_price)
print(final_price)
