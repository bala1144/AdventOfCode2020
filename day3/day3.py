
def input_parser(input_file):

    with open(input_file) as f:
        input_list = f.read().split('\n')

    print(len(input_list))
    return input_list

def traverse_map(grid, dx, dy):
    """
    parsed_map : list : can be treated as map of x,y
                #  represents tree
                .  represents openspace 
    dx : slope direction in x : column
    dy : slope direction in y : row
    """

    trees = 0
    curr_x = curr_y = 0
    grid_width = len(grid[0])

    while(len(grid) > curr_y ):
        
        trees += grid[curr_y][curr_x] == '#'
     
        curr_y += dy
        # handle the edge grid case
        curr_x = (curr_x + dx) % grid_width
        # print(curr_x, curr_y)

    return trees      


def main():
    input_file = 'D:\Projects\AdventOfCode2020\day3\input.txt'
    grid = input_parser(input_file)

    # puzzle 1
    print('number of trees ',traverse_map(grid=grid, dx=3, dy=1) )

    # puzzle 2
    dx_list = [1,3,5,7,1]
    dy_list = [1,1,1,1,2]
    tree_product = 1
    for dx,dy in zip(dx_list, dy_list ):
        tree_product *= traverse_map(grid=grid, dx=dx, dy=dy)

    print('product trees',tree_product )

if __name__ == "__main__":
    main()