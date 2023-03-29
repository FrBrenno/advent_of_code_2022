# Advent of Code 2022 - BFR

In order to practice programming and to be challenged, I decided to solve all the puzzles of the advent of code 2022 (I know I am late). 

# Report

## DAY 1 - Calorie Counting 

| Criteria | Score | Comments |
| :---: | :---: | :---: |
| Difficulty | 3/10 | Necessary to understand the puzzle that are coming|
| Technical | 4/10 | Read a file and parse correctly each line|
| Fun | 5/10 | It is no fun but it is only the beginning|
| Tries | 5, 2 | Ya, easy but not basic |

## DAY 2 - Rock Paper Scissors

| Criteria | Score | Comments |
| :---: | :---: | :---: |
| Difficulty | 1/10 | A lot easier than the first one|
| Technical | 2/10 | Read a file, parse correctly each line, implement Rock Paper Scissors rules|
| Fun | 6/10 | Implement the rules of the games was fun, idk |
| Tries | 4, 2 | To be honest, I did not count it |

## DAY 3 - Rucksack Reorganization

| Criteria | Score | Comments |
| :---: | :---: | :---: |
| Difficulty | 4/10 | difficulty was in how to get the repeated letter |
| Technical | 3/10 | Read a file, parse correctly each line, basics of ASCII|
| Fun | 5/10 | kinda a cool, kinda boring |
| Tries | 6, 4 | To be honest, I did not count it |

## DAY 4 - Camp Cleanup

| Criteria | Score | Comments |
| :---: | :---: | :---: |
| Difficulty | 5/10 | I spent some time drawing bunch of sets and theirs intersection but once you identified all, it is easier |
| Technical | 2/10 | Read a file, parsing each line to get the correct values|
| Fun | 6/10 | interesting |
| Tries | 6, 4 | To be fair, I needed a hint to get it right |

## DAY 5 - Supply Stacks

| Criteria | Score | Comments |
| :---: | :---: | :---: |
| Difficulty | 7/10 | Parsing is pretty hard and store this data in the memory in a convenient way is not obvious |
| Technical | 6/10 | Read a file, PARSING, move crates|
| Fun | 8/10 | Much more challenging and pretty satisfactory to solve |
| Tries | > 15 | I used a code of someone else to get the right answer that I tried myself to code it and get it right |

#### How to solve

1. Parse the input file
   - The file is divided in two: the first part contains the original configuration of the stacks and the second contains the sequence of movement operations that should be done.
   - The file is divided by a double '\n'
   - Try to put the original configuration in a list of stacks where each stack correspond to a column of the configuration and the last element of a stack is the top one, thus the first to be moved. This way we could easily implement the move operation
2. Create Stacks
    - Harder to do in this puzzle
    - First, you need to split, with sep='\n', the string of the configuration obtained in the last step.
    - As so we get each line, but we want to get the columns. 
    - So, inverse the order of the list to start from the bottom crates instead of the top one.
    - For each line, assign each element to a correspondent stack with a for enumerate function
    - append to the correct stack the element
    - This code is a involontary courtesy of KorigamiK
3. Parse the operations
   - Easier to do
   - Split the string with sep='\n' 
   - For each line, split it with sep=' ' and append to the operation list only the numeric element.
   - if the size of the operation is equals to 3 (quantity, source stack, destination stack), append the operation to the list of operation and clear the operation
   - iterate over all lines
4. Move
   - Part I: CrateMove9000 -> one element at a time
     - add the destination stack the last element of the source stack (the top crates) for quantity iterations
   - Part II: CrateMove9001 -> quantity elements at a time
     - use a tmp list that will save the element coming from the source stacks in the order that they should be placed in the destination stack
     - iterate over the tmp list and add all its elements to dest stack
5. Solution
    - Print the last crate/element of each stack

## DAY 6 - Tuning Trouble

| Criteria | Score | Comments |
| :---: | :---: | :---: |
| Difficulty | 1/10 | Not difficult at all, just need to go through list |
| Technical | 1/10 | Nothing different of the basics |
| Fun | 3/10 | too simple/easy |
| Tries | 1 | Oh yeah baby |
| Time spent | 30 min| |

#### How to solve

1. Parse the input file
    - The input is a single string
    - Store each character of the string a list
2. Search for the marker
    - PART I:
        - Go through the list analysing a sublist of four element
        - To verify if it is a marker: is_marker
        - if it is a marker, there is no repeated characters
        - we can create a set of this list because it will only contain one time each character
        - if the size of the size is the same as the size of the list => All characters are differents
        - The index found is for the first element in the sublist. Meanwhile the index needed in the answer if the index of the last element => just add four to it.
    - PART II:
      - The same thing but instead of a sublist of size 4, it is size 14.
      - So, the function that searches for the marker may be modified to take into account how much distinct characters is needed.
