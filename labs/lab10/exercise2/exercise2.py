num_days = int(input())
danger_threshold = float(input())
danger_days = 0
total_temp = 0
for temperature in range (num_days):
    days_temperature=float(input())
    if days_temperature > danger_threshold:
          danger_days += 1
    total_temp = total_temp + days_temperature
average_temp = total_temp / num_days
 

print(danger_days)
print(f"{average_temp:.1f}") 
