def picky_piggy(score):
    """Return the points scored from rolling 0 dice.

    score:  The opponent's current score.
    """
    # BEGIN PROBLEM 2
    #if statement for total points, add together dice rolls IF none of the dice rolls = 1
    if score == 0:
        return 7
    else:
        score = score % 6
        if score == 0:
            return 7
        elif score == 1:
            return 1
        elif score == 2:
            return 4
        elif score == 3:
            return 2
        elif score == 4:
            return 8
        elif score == 5:
            return 5

print(picky_piggy(80))