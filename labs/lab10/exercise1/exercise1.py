num_rounds = int(input())

final_score = 0
rounds_processed = 0

for num_rounds in range (num_rounds):
    score = float(input())
    if score > 100:
      rounds_score = score + (score * 0.2)

    else:
      rounds_score = score
    final_score = final_score + rounds_score 
    rounds_processed = rounds_processed + num_rounds
print(f"{final_score:.1f}")   
print(rounds_processed)

#try