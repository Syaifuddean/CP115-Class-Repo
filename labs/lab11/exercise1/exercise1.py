speed = int(input())

total_readings = 0
longest_streak = 0


while speed >= 0:
 total_readings = total_readings + 1
 if speed < 20:
       
   longest_streak += streak
speed = int(input())


print(total_readings)
print(longest_streak)














'''
# Sentinel-controlled approach - stop when ready
total = 0
count = 0

number = int(input("Enter number (0 to stop): "))  # Prime input

while number != 0:  # Condition
    total += number
    count += 1
    number = int(input("Enter number (0 to stop): "))  # Update

print(f"Total of {count} numbers: {total}")'''

#sYAIFUDDEAN