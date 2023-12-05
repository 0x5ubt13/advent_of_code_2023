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
    index_row = 0
    numbers_map = {}
    """
    numbers_map{
        index X: nums[
            {
                digits: "",
                position: [Y, Y, Y]
            },
            {
                digits: "",
                position: [Y, Y, Y]
            }]
        }  
    """
    for row in range(len(f)):
        nums_row = []
        new_num = {"digits": "", "position": []}
        index_column = 0
        previous = "."
        for col in f[row]:
            if col.isalnum():
                new_num["digits"] += col
                new_num["position"].append(index_column)
            else:
                if previous.isalnum():
                    nums_row.append(new_num)
                    new_num = {"digits": "", "position": []}
            index_column += 1
            previous = col

        # If there's a number dwindling without having been added, add it before the row is over
        if new_num["digits"] != "":
            nums_row.append(new_num)
            new_num = {"digits": "", "position": []}
        numbers_map[index_row] = nums_row
        index_row += 1
    
    return numbers_map


def assign_coordinates(grid, x, y):
    # Assign coordinates
    valid_coordinates = []

    try: 
        # up
        valid_coordinates.append(grid[x][y-1])    
    except: IndexError

    try: 
        # up - left
        valid_coordinates.append(grid[x-1][y-1])    
    except: IndexError
    
    try: 
        # left
        valid_coordinates.append(grid[x-1][y])    
    except: IndexError
    
    try: 
        # down - left
        valid_coordinates.append(grid[x-1][y+1])    
    except: IndexError
    
    try: 
        # down
        valid_coordinates.append(grid[x][y+1])    
    except: IndexError
    
    try: 
        # down - right
        valid_coordinates.append(grid[x+1][y+1])    
    except: IndexError
    
    try: 
        # right
        valid_coordinates.append(grid[x+1][y])    
    except: IndexError
    
    try: 
        # up - right
        valid_coordinates.append(grid[x+1][y-1])    
    except: IndexError

    return valid_coordinates

def solve_try2(grid, numbers_dict):
    total = 0
    
    # Loop through the entries of the dictionary and check surroundings. If symbol detected, sum the number
    for x, numbers in numbers_dict.items():
        for number in numbers:
            found = False
            for y in number["position"]:
                # print(f"row {x+1}, number {number}, y: {y}")

                # Assign coordinates
                coordinates = assign_coordinates(grid, x, y)

                # Check coordinates
                for coord in coordinates:
                    if not coord.isalnum() and coord != "." and not found:
                        # print(f"Symbol detected: {coord} | x: {x+1}, number: {number}, y: {y}")
                        total += int(number["digits"])
                        found = True
                        break
                
            # if not found:
                # print(f"row: {x} | number {number['digits']} not found")

    
    print(total)

    # 550435 low

    # return total


def main():
    with open("input_03.txt", "r") as f:
        grid = parse_file(f)
        numbers = parse_numbers(grid)
        # solve(grid, numbers)
        solve_try2(grid, numbers)




if __name__ == '__main__':
    main()