"""Advent of Code 2022 - DAY 6 - Tuning Trouble"""
INPUT_FILE="./data/input_6.txt"


def is_marker(string):
    return len(set(string)) == len(string)

def search_marker(signal, distinct_char):
    for index in range(0, len(signal)-1):
        marker = signal[index:index+distinct_char]
        if is_marker(marker):
            return index + distinct_char

def challenge_1():
    signal = []
    with open(INPUT_FILE) as input:
        for char in input.read():
            signal.append(char)
    packet_index = search_marker(signal, 4)
    message_index = search_marker(signal, 14)
    print("Answer: ", packet_index)
    print("Answer: ", message_index)


if __name__ == "__main__":
    challenge_1()