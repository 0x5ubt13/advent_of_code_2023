def parse_file(f):
    grid = []
    for row in f:
        grid.append([col for col in row.strip()])

    return grid


def parse_grid(grid):
    total = 0
    for row in range(len(grid)):
        print("row", row)
        for col in range(len(grid)):
            if grid[row][col] != "." and grid[row][col].isnumeric() == False:
                print(f"symbol {grid[row][col]} found at {row, col}")

                if grid[row-1][col-1].isnumeric():
                    total += int(grid[row-1][col-1])

                    total += int(grid[row-1][col])

                    total += int(grid[row-1][col+1])

                    total += int(grid[row][col-1])

                    total += int(grid[row][col+1])
                
                    total += int(grid[row+1][col+1])

                    total += int(grid[row+1][col])

                    total += int(grid[row+1][col-1])

    print(total)

def main():
    with open("./test_input_03.txt", "r") as f:
        parse_grid(parse_file(f))
    


if __name__ == '__main__':
    main()