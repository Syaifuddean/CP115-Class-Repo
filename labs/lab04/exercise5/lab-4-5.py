scoreA = int(input())
scoreB = int(input())
if scoreA == scoreB:
    pointsA = 1
    pointsB = 1
else:
    if scoreA < scoreB:
        pointsB = 3
        pointsA = 0
    else:
        if scoreA == 0:
            pointsB = 1
        else:
            if scoreB == 0:
                pointsA = 1
        pointsA = 3
        pointsB = 0
finalPointsA = pointsA + pointsA + pointsA + pointsA
finalPointsB = pointsB + pointsB + pointsB + pointsB
print(finalPointsA)
print(finalPointsB)
