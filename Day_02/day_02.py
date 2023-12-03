#!/usr/bin/python3

def parse_games(f):
    total, powers, max_red, max_green, max_blue = 0, 0, 12, 13, 14

    for game in f:
        max_red_seen, max_green_seen, max_blue_seen = 0, 0, 0
        impossible_game = False
        game_id = game.strip().split(":")[0].split(" ")[1]
        sets = game.strip().split(":")[1].split(";")

        for set in sets:
            set_cubes = set.split(",")

            for cubes in set_cubes:
                number_colour = cubes.split(" ")
                if "blue" in number_colour[2]:
                    if int(number_colour[1]) > max_blue_seen:
                        max_blue_seen = int(number_colour[1])
                    if int(number_colour[1]) > max_blue:
                        impossible_game = True
      
                if "red" in number_colour[2]:
                    if int(number_colour[1]) > max_red_seen:
                        max_red_seen = int(number_colour[1])
                    if int(number_colour[1]) > max_red:
                        impossible_game = True
                        
                if "green" in number_colour[2]:
                    if int(number_colour[1]) > max_green_seen:
                        max_green_seen = int(number_colour[1])
                    if int(number_colour[1]) > max_green:
                        impossible_game = True

        if not impossible_game:
            total += int(game_id)

        powers += max_blue_seen * max_green_seen * max_red_seen

    return total, powers

def main():
    with open("./input_02.txt") as f:
        part_1, part_2 = parse_games(f)

    print(f"Part 1 solution: {part_1}. Part 2 solution: {part_2}")

if __name__ == '__main__':
    main()