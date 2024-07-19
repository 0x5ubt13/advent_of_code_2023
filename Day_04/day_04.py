total_count = 0

with open("Day_04/day_04_input.txt", "r") as f:
    for line in f:
        line = line.strip()
        print(line)

        left = line.split(" | ")[0].split(":")[1].split(" ")
        right = line.split(" | ")[1].split(" ")

        count = 0
        for num in left:
            if not num.isalnum():
                continue
            if num in right:
                if count == 0:
                    count = 1
                else: 
                    count *= 2
                print(f"left: {left}, right: {right}, num: {num}")
        total_count += count

    print(f"Part 1 -> {total_count}")

    