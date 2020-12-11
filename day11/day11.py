from itertools import product
import copy

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n')

    input_list = [ list(line[:]) for line in input_list]
    return input_list

def compose_dirs(grid, row, col):

    rows = [-1,0,1]
    cols = [-1,0,1]
    
    # handle edge cases
    if row == 0:
        rows.remove(-1)
    elif row == len(grid)-1:
        rows.remove(1)
    
    # handle edge cases
    if col == 0:
        cols.remove(-1)
    elif col ==  len(grid[0])-1 :
        cols.remove(1)

    dirs = list(product(rows, cols))
    dirs.remove((0,0))
    return dirs

def get_adjacent_seat(grid, row, col):
  
    # get the adjacent element
    # y for y in a if y not in b
    # print('row', row, 'col', col)
    # print('rows', rows, 'cols', cols)
    dirs = compose_dirs(grid,row, col)
    adjacent_seats = [ grid[row + x][col + y] for x,y in dirs ]
    return adjacent_seats

def get_first_adjacent_seat(grid, row, col):
    """ Get the first adjacent seats on the all eight directions

    Rule:
    instead of considering just the eight immediately adjacent seats, 
    consider the first seat in each of those eight directions. For example,
    the empty seat below would see eight occupied seats:
    
    """
    grid_len, grid_width = len(grid), len(grid[0])
    dirs = compose_dirs(grid,row, col)
    neighours = []
    for dx,dy in dirs:
        curr_x, curr_y = row + dx, col + dy
        # print(curr_x,curr_y, dx, dy)
        while curr_x in range(0, grid_len) and curr_y in range(0,grid_width):
            next_element =  grid[curr_x][curr_y]
            if next_element != '.':
                neighours.append(next_element)
                break

            curr_x, curr_y =  curr_x + dx , curr_y + dy 

    return neighours

def fill_seats(grid):
    """Fill the seat based on the first rule that
    
    "If a seat is empty (L) and there are no occupied seats
     adjacent to it, the seat becomes occupied"

    """
    grid_width = len(grid[0])
    new_grid = copy.deepcopy(grid)

    for row in range(len(grid)):
        for col in range(grid_width):
            if grid[row][col] == 'L':
                adjacent_seats = get_adjacent_seat(grid,row,col)
                if 'L' in adjacent_seats:
                    new_grid[row][col]='#' 
    

    return new_grid

def display(grid):
    print()
    for row in grid:
        print(row)

def empty_seats(grid):
    """Empty the seat based on the rule
    
    "If a seat is occupied (#) and four or more seats adjacent to it 
    are also occupied, the seat becomes empty."

    """
    grid_width = len(grid[0])
    new_grid = copy.deepcopy(grid)

    for row in range(len(grid)):
        for col in range(grid_width):
            if grid[row][col] == '#':
                adjacent_seats = get_adjacent_seat(grid,row,col)
                # if col == 6 and row == 0:
                #     print('adjacent_seats', adjacent_seats)
                
                if adjacent_seats.count('#') >= 4:
                    new_grid[row][col]='L'

    return new_grid

def simulate_people(grid, max_occupied_seats = 4, find_seat_fn=get_adjacent_seat):

    grid_width = len(grid[0])
    old_filled_seat = -1

    while True : 
        new_grid = copy.deepcopy(grid)
        for row in range(len(grid)):
            for col in range(grid_width):
                adjacent_seats = find_seat_fn(grid,row,col)
                if grid[row][col] == 'L' and '#' not in adjacent_seats:
                    new_grid[row][col]='#' 
                elif grid[row][col] == '#' and adjacent_seats.count('#') >= max_occupied_seats :
                    new_grid[row][col]='L'

        # display(new_grid)
        filled_seat = sum([row.count('#') for row in new_grid])
     
        if filled_seat == old_filled_seat:
            break

        # set new grid to old grid
        grid = copy.deepcopy(new_grid)
        old_filled_seat = filled_seat
    
    print('Number of filled seats ', filled_seat) 

def main():
    # input_file = 'D:\Projects\AdventOfCode2020\day11\sample_input.txt'
    input_file = 'D:\Projects\AdventOfCode2020\day11\input.txt'
    grid = input_parser(input_file) 
    # print(grid)

    # puzzle 1
    # simulate_people(grid)
    # display(grid)

    # puzzle 2
    simulate_people(grid, max_occupied_seats=5, find_seat_fn=get_first_adjacent_seat)
    # display(grid)
if __name__ == "__main__":
    main()