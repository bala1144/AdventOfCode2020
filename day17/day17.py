import itertools
import numpy as np
from collections import defaultdict
import copy

def input_parser(input_file):
    """Read the input and define the basic grid structure
    
    The pocket dimension contains an infinite 3-dimensional grid. 
    At every integer 3-dimensional coordinate (x,y,z), there exists
    a single cube which is either active or inactive.

    """
    with open(input_file) as f:
        input_list = f.read().split('\n')
    
    grid = defaultdict(lambda: 0)

    for y in range(len(input_list)):
        for x in range(len(input_list[0])):
            if input_list[y][x] == '#':
                grid[(0,0,y,x)] = 1
    grid_size=(0,0,y,x) # w,z,y,x
    return grid, grid_size

def get_neighbours(dims = 3):
    """ get the general directions for the neighbour

    Each cube only ever considers its neighbors: any of the 26 other cubes where any of their 
    coordinates differ by at most 1. For example, given the cube at x=1,y=2,z=3, its neighbors
    include the cube at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.

    """

    neighbout_dirs = []
    for dirs in itertools.product([-1,0,1], repeat=dims):
        if np.count_nonzero(np.array(dirs)) > 0:
            if dims == 3:
                dirs = tuple([0] + list(dirs)) # if dim = 3, dirs(x,y,z) hence adding 0 for w dimension
            neighbout_dirs.append(dirs)
    return neighbout_dirs

def count_neighbours(point, grid,neighbout_dirs, dim=3):
    count = 0
    for dirs in neighbout_dirs:
        neighbor_cube = tuple( x+y for x,y in zip(point, dirs))
        count += grid[neighbor_cube]

    return count

def simulate_energy_cycles(grid, grid_size, dim=3, numOfcycles=6):
    """Similuate energy cycles based on the rules

    During a cycle, all cubes simultaneously change their state according 
    to the following rules:

    If a cube is active and exactly 2 or 3 of its neighbors are also active, 
    the cube remains active. Otherwise, the cube becomes inactive.
    If a cube is inactive but exactly 3 of its neighbors are active, 
    the cube becomes active. Otherwise, the cube remains inactive.

    """
    # get neighbour dirs
    neighbout_dirs = get_neighbours(dim)
    gw, gz, gy, gx = grid_size
    dw = range(0,1)
    
    # create a new grid
    for i in range(1,numOfcycles+1):
        
        new_grid = defaultdict(lambda: 0)
        
        if dim==4:
            dw = range(-i, gw+i+1) 
        for w in dw:
            for z in range(-i, gz+i+1):
                for y in range(-i, gy+i+1): # (3,3)
                    for x in range(-i, gx+i+1):
                        point = (w,z,y,x)
                        num_neighbours = count_neighbours( point ,grid, neighbout_dirs )
                        if grid[point] == 1 and num_neighbours in [2,3]:
                            new_grid[point] = 1
                        elif grid[point] == 0 and num_neighbours == 3:
                            new_grid[point] = 1
            # print(i, len(new_grid))
        # print(new_grid)
        grid = copy.deepcopy(new_grid)
    
    return len(new_grid)

def main():
    input_file = 'D:\Projects\AdventOfCode2020\day17\sample_input.txt'
    # input_file = 'D:\Projects\AdventOfCode2020\day17\input.txt'
    grid, grid_size = input_parser(input_file)
    print('Puzzle 1 3D', simulate_energy_cycles(grid, grid_size, dim=3))
    print('Puzzle 1 4D', simulate_energy_cycles(grid, grid_size, dim=4))

if __name__ == "__main__":
    main()