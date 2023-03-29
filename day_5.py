"""Advent of Code - DAY 5 - Supply Stacks"""

INPUT_FILE="./data/input_5.txt"

def create_stacks(configuration_str):
    """Code borrowed from KorigamiK
    https://gitlab.com/KorigamiK/advent-of-code/-/blob/main/5.py
    """
    *crates, num_stacks = configuration_str.split("\n")
    
    nb_stacks = len(num_stacks.split())
    
    stacks = [[] for _ in range(nb_stacks)]
    crates.reverse()
    for line in crates:
        for stack_idx, i in enumerate(range(1, len(crates[0]), 4)):
            if line[i].strip():
                stacks[stack_idx].append(line[i])
    return stacks

def parse_operations(operations_str):
    list_operations = []
    operation = []
    for line in operations_str.split("\n"):
        for elem in line.split(" "):
            if elem.isnumeric():
                operation.append(int(elem))
            if len(operation) == 3:
                list_operations.append(operation)
                operation = []
    return list_operations
            
def move_CreateMove9000(stacks, operation):
    quantity, src_nb, dest_nb = operation
    src_stack = stacks[src_nb-1]
    dest_stack = stacks[dest_nb-1]
    for _ in range(quantity):
        dest_stack.append(src_stack.pop())              

def move_CreateMove9001(stacks, operation):
    quantity, src_nb, dest_nb = operation
    src_stack = stacks[src_nb-1]
    dest_stack = stacks[dest_nb-1]
    tmp = []
    for _ in range(quantity):
        tmp.append(src_stack.pop())
    tmp.reverse()
    for elem in tmp:
        dest_stack.append(elem)
    
        
def print_top_crates(stacks):
    print("Answer: ", end="")
    for stack in stacks:
        print(stack[-1], end="")
    print()
    
def challenge_1_2():
    print("### DAY 5 - Supply Stacks ###")
    original_configuration = ""
    operations = ""
    with open(INPUT_FILE) as input:
        original_configuration, operations = input.read().split("\n\n")
    stacks_1 = create_stacks(original_configuration)
    stacks_2 = create_stacks(original_configuration)
    list_operations = parse_operations(operations)
    for operation in list_operations:
        move_CreateMove9000(stacks_1, operation)  # Part 1
        move_CreateMove9001(stacks_2, operation)  # Part 2
    print_top_crates(stacks_1)
    print_top_crates(stacks_2)



if __name__ == "__main__":
    challenge_1_2()