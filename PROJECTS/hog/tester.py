from hog import play, always_roll
from dice import make_test_dice



"""CS 61A Presents The Game of Hog."""
import hog
from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    #roll dice function 2 args returns number of points 
    #storage variables 
    score = []
    rick_rolls = 0 
    new_points = 0
    while num_rolls > rick_rolls:
        new_points = dice()
        score.append(new_points)
        rick_rolls += 1
    for i in score:
        if i == 1:
            return 1
    else: 
        return sum(score) 
        
        

    # make a while loop for the length of num rolls 

    #store num rolls so it can be passed into other functions 


    # END PROBLEM 1


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

    # END PROBLEM 2


def take_turn(num_rolls, opponent_score, dice=six_sided, goal=GOAL_SCORE):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 in the case
    of a player using Picky Piggy.
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    goal:            The goal score of the game.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < goal, 'The game should be over.'
    # BEGIN PROBLEM 3
    if num_rolls == 0:
        return picky_piggy(opponent_score)
    else: 
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def hog_pile(player_score, opponent_score):
    """Return the points scored by player due to Hog Pile.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.
    """
    # BEGIN PROBLEM 4
    if player_score == opponent_score:
        return player_score
    else:
        return 0
        
    # END PROBLEM 4


def next_player(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> next_player(0)
    1
    >>> next_player(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    # TAKE BOTH SCORE 1 AND SCORE 0 AS INPUTS FOR STRATEGY
    while max(score0, score1) < goal:
        if who == 0: 
            score0 += take_turn(strategy0(score0, score1), score1, dice, goal)
            score0 += hog_pile(score0, score1)
        elif who == 1:
            score1 += take_turn(strategy1(score1, score0), score0, dice, goal)
            score1 += hog_pile(score1, score0)
        who = next_player(who)  
        say = say(score0, score1)
    return score0, score1

    
def echo(s0, s1):
        print(s0, s1)
    return echo 
    
strat0 = lambda score, opponent: 1 - opponent // 10
strat1 = always_roll(3)
s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)