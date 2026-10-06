grade = float(input())
total_score = 0
valid_count = 0
average = 0
while grade != -1:
    if grade < 0 or grade > 100:
            grade = float(input())  
            continue
    valid_count += 1
    total_score += grade

average = total_score / valid_count


print(valid_count)
print(f"{average:.2f}")
