total_count = 0

with open("Day_04/day_04_input.txt", "r") as f:
    for line in f:
        line = line.strip()
        # print(line)

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
                # print(f"left: {left}, right: {right}, num: {num}")
        total_count += count

    print(f"Part 1 -> {total_count}")


"""
There's no such thing as "points". 
Instead, scratchcards only cause you to win more scratchcards equal to the number of winning numbers you have.

Specifically, you win copies of the scratchcards below the winning card equal to the number of matches. 
So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. 
So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards 
that the original card 10 won: cards 11, 12, 13, 14, and 15. 
This process repeats until none of the copies cause you to win any more cards. 
(Cards will never make you copy a card past the end of the table.)


    Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
    Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
    Your copy of card 2 also wins one copy each of cards 3 and 4.
    Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
    Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
    Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
    Your one instance of card 6 (one original) has no matching numbers and wins no more cards.

    Once all of the originals and copies have been processed, you end up with 
    1 instance of card 1, 
    2 instances of card 2, 
    4 instances of card 3, 
    8 instances of card 4, 
    14 instances of card 5, 
    and 1 instance of card 6. 
    In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

Process all of the original and copied scratchcards until no more scratchcards are won. 
Including the original set of scratchcards, how many total scratchcards do you end up with?
"""

index = 0
index_dict = {}
for i in range(1000):
    index_dict[i] = 1

total_count = 0
with open("Day_04/day_04_input.txt", "r") as f:
    for line in f:
        index += 1
        line = line.strip()
        # print(line)

        left = line.split(" | ")[0].split(":")[1].split(" ")
        right = line.split(" | ")[1].split(" ")

        count = 0
        for num in left:
            if not num.isalnum():
                continue
            if num in right:
                count += 1
        for k in range(index_dict[index]):
            for i in range(count):
                # print(f"index_dict[{index+i+1}] += 1")
                index_dict[index+i+1] += 1

        # print(f"index_dict[{index}] = {index_dict[index]}")
        count *= index_dict[index]
        total_count += count + 1

print("Part 2 ->", total_count)


