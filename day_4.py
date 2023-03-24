""" Advent of Code 2022 - DAY 4
In how many assignment pairs does one range fully contain the other?
"""

with open(r"./data/input_4.txt") as input:
    subsets = 0
    overlaps = 0
    for pair in input.readlines():
        assignement_1, assignement_2 = pair.split(",")
        lowerbound_1, upperbound_1 = assignement_1.split("-")
        lowerbound_2, upperbound_2 = assignement_2.split("-")
        lowerbound_1, lowerbound_2 = int(lowerbound_1), int(lowerbound_2)
        upperbound_1, upperbound_2 = int(upperbound_1), int(upperbound_2)
        if lowerbound_1 == lowerbound_2:
            subsets += 1
        else:
            if lowerbound_1 < lowerbound_2:  # assignment 1 is bigger than assignement 2
                if upperbound_1 >= upperbound_2:
                    subsets += 1
                elif lowerbound_2 <= upperbound_1:
                    overlaps += 1
            else:  # assignment 2 is bigger than assignement 1
                if upperbound_2 >= upperbound_1:
                    subsets += 1
                elif upperbound_2 >= lowerbound_1:
                    overlaps += 1
        overlaps += subsets

    print(f"Total subsets: {subsets}")
    print(f"Total overlaps: {overlaps}")
