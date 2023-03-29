"""Adventure of Code - DAY 2 - Rock Paper Scissors
First Column is your opponent choice
Second Column is your choice
What would your total score be if everything goes exactly according to your strategy guide?

First Column is your opponent choice
Second Column is the round outcome
Following the Elf's instructions for the second column, what would your total score be if
everything goes exactly according to your strategy guide?
"""
def should_i_play(outcome, opponent):
    """ X : Lose
        Y : Draw
        Z : Win    
        --------
        A/X: Rock
        B/Y: Paper
        C/Z: Scissors
    """
    if outcome == "X": #In losing round
        if opponent == "A":
            return "Z"
        elif opponent == "B":
            return "X"
        else:
            return "Y"
    elif outcome == "Y": # In draw round
        if opponent == "A":
            return "X"
        elif opponent == "B":
            return "Y"
        else:
            return "Z"
    else:
        if opponent == "A":
            return "Y"
        elif opponent == "B":
            return "Z"
        else:
            return "X"
            

def result(opponent, me):
    """ A/X: Rock
        B/Y: Paper
        C/Z: Scissors
    """
    if (me == "X" and opponent == "A") or (me == "Y" and opponent == "B") or (me == "Z" and opponent == "C"):
        # Draw
        return 0
    elif (me == "X" and opponent == "C") or (me == "Y" and opponent == "A") or (me == "Z" and opponent == "B"):
        # I won
        return 1
    else: 
        # I lost
        return -1


with open("./data/input_2.txt") as input:
    total_score = 0
    for round in input.readlines():
        score = 0
        data = round.split(" ")
        opponent = data[0].strip()
        outcome_data = data[1].strip()
        me = should_i_play(outcome_data, opponent)
        round_result = result(opponent, me)
        
        if round_result == 0:
            score += 3 # Draw
        elif round_result == 1:
            score += 6 # Won the round
        if (me == "X"):
            score += 1 # If I am rock
        elif (me == "Y"):
            score += 2 # If I am Paper
        elif (me == "Z"):
            score += 3 # If I am Scissor 
        total_score += score
    
    print(f"Total score following the strategy: {total_score}")
