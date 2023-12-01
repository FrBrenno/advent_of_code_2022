"""Advent of Code 2022 - DAY 1
Find the Elf carrying the most Calories. 
How many total Calories is that Elf carrying?

Find the top three Elves carrying the most Calories. 
How many Calories are those Elves carrying in total?
"""
top_calorie = [0]
with open("./data/input_1.txt") as input:
    lines = input.readlines()  # Read all lines
    elf_number = 0
    calorie = 0  # Total of calories thats one elf is carrying
    for line in lines:
        if "\n" == line:  # Passage au prochain elf
            if (calorie > top_calorie[0]): 
                top_calorie.append(calorie) #Added to the list only the maximum
            elf_number += 1
            calorie = 0
        else:
            calorie += int(line)
    top_calorie.sort(reverse=True) #Descending order
    print(f"The top one elf is carrying {top_calorie[0]} calories")
    print(f"The top three elf are carrying {sum(top_calorie[:3])} calories")
