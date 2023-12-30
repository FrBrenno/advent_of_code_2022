"""
Day 2: Cube Conundrum - 56:15 min

Part 1 Description:
The Elf would first like to know which games would have been possible if the bag contained only
12 red cubes, 13 green cubes, and 14 blue cubes?

Determine which games would have been possible if the bag had been loaded with only 12 red cubes,
13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

Part 2 Description:
What is the fewest number of cubes of each color that could have been in the bag to make the game possible?
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
What is the sum of the power of these sets?
"""
RUN_TEST_FILE = False
filepath = "./data/input_day_2_test.txt" if RUN_TEST_FILE else "./data/input_day_2.txt"

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

def part1():
    with open(filepath, "r") as f:
        data = f.readlines()
        total = 0
        for game_id, line in enumerate(data):
            acceptable = True   
            game = line.split(":")[1]
            subsets = game.split(";")
            for subset in subsets:
                cubes = subset.split(",")
                for cube in cubes:
                    vide, number, color = cube.split(" ")
                    if "\n" in color:
                        color = color[:-1]
                    if color == "red" and int(number) > MAX_RED_CUBES:
                        acceptable = False
                        break
                    if color == "green" and int(number) > MAX_GREEN_CUBES:
                        acceptable = False
                        break
                    if color == "blue" and int(number) > MAX_BLUE_CUBES:
                        acceptable = False
                        break
                if not acceptable:
                    break
            if acceptable:
                total += game_id+1
        print("Answer: The sum of IDs of acceptable games is: ", total)
                    

def part2():
    with open(filepath, "r") as f:
        data = f.readlines()
        total = 0
        for line in data:
            max_red = 0
            max_green = 0
            max_blue = 0
            game = line.split(":")[1]
            subsets = game.split(";")
            for subset in subsets:
                cubes = subset.split(",")
                for cube in cubes:
                    vide, number, color = cube.split(" ")
                    if "\n" in color:
                        color = color[:-1]
                    if color == "red":
                        max_red = int(number) if int(number) > max_red else max_red
                    if color == "green":
                        max_green = int(number) if int(number) > max_green else max_green
                    if color == "blue":
                        max_blue = int(number) if int(number) > max_blue else max_blue  
            power = max_red * max_green * max_blue
            total += power
        print("Answer: The sum of power of these set is: ", total)

if __name__ == '__main__':
    print("#"*10, "DAY 2", "#"*10)
    print("#"*10, "PART 1", "#"*10)
    part1()
    print("#"*10, "PART 2", "#"*10)
    part2()