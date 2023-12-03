#!/usr/bin/python3

def part_one():
    # Declare array that will hold the puzzle numbers
    numbers = []

    # Read input and operate through the words
    with open("./input_01.txt", "r") as f:
        for word in f:
            # Declare index and array to get numbers from word
            index = 0
            count = 0
            number = [0, 0]

            for char in word:
                if char.strip().isnumeric():
                    number[index] = char
                    index = 1
                    count += 1
            
            if count == 1:
                number[1] = number[0]
            numbers.append(int(f'{number[0]}{number[1]}'))
        
        print(f'Part 1 solution: {sum(numbers)}')


def parse_line(word):
    new_word = ""
    index = 0
    while index <= len(word)-1:
        match word[index]:
            case "o":
                try:
                    if word[index+1] == "n" and word[index+2] == "e":
                        new_word += "1"
                        index += 2
                        continue
                except: IndexError
                
            case "t":
                try:
                    if word[index+1] == "w" and word[index+2] == "o":
                        new_word += "2"
                        index += 2
                        continue

                    if word[index+1] == "h" and word[index+2] == "r" and word[index+3] == "e" and word[index+4] == "e":
                        new_word += "3"
                        index += 4
                        continue
                except: IndexError

            case "f":
                try:
                    if word[index+1] == "o" and word[index+2] == "u" and word[index+3] == "r":
                        new_word += "4"
                        index += 3
                        continue

                    if word[index+1] == "i" and word[index+2] == "v" and word[index+3] == "e":
                        new_word += "5"
                        index += 3
                        continue
                except: IndexError

            case "s":
                try:
                    if word[index+1] == "i" and word[index+2] == "x":
                        new_word += "6"
                        index += 2
                        continue
                    if word[index+1] == "e" and word[index+2] == "v" and word[index+3] == "e" and word[index+4] == "n":
                        new_word += "7"
                        index += 4
                        continue
                except: IndexError

            case "e":
                try:
                    if word[index+1] == "i" and word[index+2] == "g" and word[index+3] == "h" and word[index+4] == "t":
                        new_word += "8"
                        index += 4
                        continue
                except: IndexError
                
            case "n":
                try:
                    if word[index+1] == "i" and word[index+2] == "n" and word[index+3] == "e":
                        new_word += "9"
                        index += 3
                        continue
                except: IndexError

        # If arrived down here, default
        new_word += word[index]
        index += 1
    
    return new_word 

def part_two():
    # Declare array that will hold the puzzle numbers
    numbers = []

    # Read input and operate through the words
    with open("./input_01.txt", "r") as f:
        for word in f:
            # Part 2: read line and convert written numbers to arabic numbers
            l = parse_line(word)
            print(word)
            print(l)

            # Declare index and array to get numbers from word
            index = 0
            count = 0
            number = [0, 0]

            for char in l:
                if char.strip().isnumeric():
                    number[index] = char
                    index = 1
                    count += 1
            
            if count == 1:
                number[1] = number[0]
            numbers.append(int(f'{number[0]}{number[1]}'))

            print(f'{number[0]}{number[1]}')
        
        print(f'Part 2 solution: {sum(numbers)}')


def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()