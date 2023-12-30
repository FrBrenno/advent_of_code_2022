"""
DAY 1

As they're making the final adjustments, they discover that their calibration document 
(your puzzle input) has been amended by a very young Elf who was apparently just excited
to show off her art skills. Consequently, the Elves are having trouble reading the values
on the document.

The newly-improved calibration document consists of lines of text; each line originally
contained a specific calibration value that the Elves now need to recover. On each line,
the calibration value can be found by combining the first digit and the last digit 
(in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. 
Adding these together produces 142.

"""

def part1():
    """
    Consider your entire calibration document. 
    What is the sum of all of the calibration values?
    """
    with open(r"./data/input_day_1.txt", "r") as f:
        data = f.readlines()
        sum = 0
        # Looking for first and last digit
        for line in data:
            first_digit = ""
            last_digit = ""
            for character in line:
                if str(character).isdigit():
                    if first_digit == "":
                        # If first digit is not found yet
                        first_digit = character
                    else:
                        # When first digit is set, find last digit
                        last_digit = character
            # Two cases:
            #   1- first and last digits are found. group them and add to the sum
            #   2- only one digit in the line. duplicate the first digit
            number = 0
            if last_digit == "":
                number = int(first_digit + first_digit)
            else:
                number = int(first_digit+last_digit)
            sum += number
                        
        print("-> The sum of all calibration values is: ", sum)
    
                    

def part2():
    """
    Your calculation isn't quite right. It looks like some of the digits are actually
    spelled out with letters: one, two, three, four, five, six, seven, eight, and nine
    also count as valid "digits".
    What is the sum of all of the calibration values?
    """
    numbers_names = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"
    }
    sum = 0
    with open(r"./data/input_day_1.txt", "r") as f:
        data = f.readlines()
        for line in data:
            # For each line, replace number names for the actual digit  
            for name, replacement in numbers_names.items():
                if name in line:
                    line = line.replace(name, name+replacement+name)         
                       
            # Search for first and last digits as for part 1
            # Find digits in the line
            digits_found = [char for char in line if char.isdigit()]
            first_digit = digits_found[0] if digits_found else ""
            last_digit = digits_found[-1] if digits_found else first_digit
            
            print(line, digits_found, first_digit, last_digit)

            number = int(first_digit + last_digit)
            sum += number     
            
        print("-> The sum of all calibration values is: ", sum)
            
                    
        

if __name__ == '__main__':
    print("#"*10, "DAY 1", "#"*10)
    print("#"*5, "PART 1", "#"*5)
    part1() # Answer: 55607
    print("#"*5, "PART 2", "#"*5)
    part2() # Answer: 54418