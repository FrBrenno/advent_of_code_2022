"""
DAY 3

Description:

The engine schematic (your puzzle input) consists of a visual representation of the engine. 
There are lots of numbers and symbols you don't really understand, but apparently any number 
adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
(Periods (.) do not count as a symbol.)

Of course, the actual engine schematic is much larger. What is the sum of all of the part
numbers in the engine schematic?

"""

TEST=True

def build_symbol_map(lines):
    res = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            char = lines[i][j]
            if not char.isdigit() and char != '.':
                res.append((i,j))
    return res

def part1():
    file_name = r"./data/input_day_3_test.txt" if TEST else r"./data/input_day_3.txt"
    tot = 0
    with open(file_name, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        
        symbols = build_symbol_map(lines)
        part_numbers = compute_part_number(lines, symbols)
        #print("line: ", line) 

def part2():
    pass

if __name__ == '__main__':
    print("#"*10, "DAY 3", "#"*10)
    print("#"*10, "PART 1", "#"*10)
    part1()
    print("#"*10, "PART 2", "#"*10)
    part2()