def parse_file(f):
    grid = []
    for row in f:
        grid.append([col for col in row.strip()])
    return grid


# def parse_grid(grid):
#     total = 0
#     for row in range(len(grid)):
#         print("row", row)
#         for col in range(len(grid)):
#             if grid[row][col] != "." and grid[row][col].isnumeric() == False:
#                 print(f"symbol {grid[row][col]} found at {row, col}")

    #             if row != 0 and int(grid[row-1][col-1]).isnumeric():
    #                 total += int(grid[row-1][col-1])

    #                 total += int(grid[row-1][col])

    #                 total += int(grid[row-1][col+1])

    #                 total += int(grid[row][col-1])

    #                 total += int(grid[row][col+1])
                
    #                 total += int(grid[row+1][col+1])

    #                 total += int(grid[row+1][col])

    #                 total += int(grid[row+1][col-1])

    # print(total)

def parse_numbers(f):
    index = 0
    numbers_map = {}
    for row in range(len(f)):
        nums = ''
        nums_row = []
        for col in f[row]:
            if col.isalnum():
                nums += col
            else:
                if nums[:-1].isalnum():
                    nums_row.append(nums)
                    nums = ''
        numbers_map[index] = nums_row
        index += 1
    
    return numbers_map


def solve(grid, numbers):
    # Loop over the rows of the grid
    for row in range(len(grid)):
        print(f"row {row}")
        # Loop over the dictionary values matching the current grid a row
        for number in numbers[row]:
            print(f"row: {row}, number: {number}")

            for digit in number:
                # Get digit position
                print(f"digit {digit}")


                # for digit in range(digits):
                    # num_position = grid[k][]
                
                # Check if number is surrounded by symbols
                

                # up, upleft, left, leftdown, down, downright, right, upright = grid[k][] 
                # if grid[]

def main():
    with open("test_input_03.txt", "r") as f:
        grid = parse_file(f)
        numbers = parse_numbers(grid)
        solve(grid, numbers)


if __name__ == '__main__':
    main()