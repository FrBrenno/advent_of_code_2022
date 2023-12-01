"""Adventure of Code 2022 - DAY 3 - Rucksack Reorganization
Find the item type that appears in both compartments of each rucksack.
What is the sum of the priorities of those item types?

Find the item type that corresponds to the badges of each three-Elf group. 
What is the sum of the priorities of those item types?
"""


def get_priority(character):
    if (character.islower()):
        return int(ord(character) - ord('a') + 1)
    elif (character.isupper()):
        return int(ord(character) - ord('A') + 27)


with open("./data/input_3.txt") as input:
    total_priority = 0
    total_badge_priority = 0
    items = []
    badges = []
    groups = []
    for rucksack in input.readlines():
        items_set = set()
        first_compartiment = rucksack[:len(rucksack)//2]
        second_compartiment = rucksack[len(rucksack)//2:-1]
        for i in first_compartiment:
            if i in second_compartiment:
                items_set.add(i)
        for i in items_set:
            items.append(i)

        # PART 2
        rucksack = rucksack[:-1]
        groups.append(rucksack)
        if len(groups) == 3:
            badges_set = set()
            for item in groups[0]:
                if item in groups[1] and item in groups[2]:
                    badges_set.add(item)
            for i in badges_set:
                badges.append(i)
            groups = []

    for i in items:
        total_priority += get_priority(i)
    for b in badges:
        total_badge_priority += get_priority(b)
    print(f"The total priority is {total_priority}")
    print(f"The total badge priority is {total_badge_priority}")
