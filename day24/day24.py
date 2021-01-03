import math 
from operator import add
from collections import defaultdict
import numpy as np
import copy

# hexagonal directions are represented by
# directions = { 
#     'e' : [1,0,0],
#     'w' : [-1,0,0],
#     'ne' :[0,0,1],
#     'nw' :[0,-1,0],
#     'se' :[0,1,0],
#     'sw' :[0,0,-1]
#  }

directions = { 
    'e' : [1,0],
    'w' : [-1,0],
    'ne' :[0.5,0.5],
    'nw' :[-0.5,0.5],
    'se' :[0.5,-0.5],
    'sw' :[-0.5, -0.5]
 }

def input_parser(input_file):
    """Read the input and get the inputs are parsing

    """
    with open(input_file) as f:
        input_list = f.read().split('\n')
    
    return input_list

def traverse_seq(seq):
    
    id = 0 
    dir_list = []
    # print(seq)
    i = 0
    while( id < len(seq)):
        dir = seq[id]     
        if dir == 'n' or dir =='s':
            dir = seq[id : id+2]
            id += 1
        
        # print(i, dir)
        # i += 1
        # add the dirs to list
        dir_list.append(directions[dir])
        id += 1

    # compute the final hexagon
    dir_list =  np.asarray(dir_list)
    final_pos = tuple(np.sum(dir_list, axis=0))
    
    return final_pos

def flip_tiles(input_list):
    """Based on the input directions flip the tiles all  the tiles start with white
    """

    grid = defaultdict(int)
    for dir_Seq in input_list:
        final_pos = traverse_seq(dir_Seq)
        grid[final_pos] += 1
    
    # extract the odd values for black tiles
    # print(grid)
    print('Number of Black Tiles',  sum([x for x in grid.values() if x%2 == 1]))
    # print('Number of set', set(grid.keys()), len(set(grid.keys())) )
    return grid 

def get_neighbours(pos, grid):
    
    pos = np.asarray(pos)
    neigbours = np.asarray(list(directions.values()))
    neigbours = pos + neigbours

    neigh_tiles = [grid[tuple(row)] for row in neigbours]
    return neigbours, neigh_tiles

def simulate_live_art(grid, days=1):
    """
    The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

    Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.

    The rules are applied simultaneously to every tile; put another way, 
    it is first determined which tiles need to be flipped, then they are all flipped at the same time.
    """

    
    print('Before start Number of Black tiles', sum([ 1 for x in grid.values() if x % 2 == 1]))     

    for day in range(1,days+1):
        grid_cpy = copy.deepcopy(grid)

        # create a list of tiles that need to be visited
        to_visit = np.asarray(list(grid_cpy.keys()))
        for tiles in grid_cpy.keys():
            neigbours, _ = get_neighbours(tiles, grid)
            to_visit = np.concatenate((to_visit, neigbours))
        to_visit = np.unique(to_visit, axis=0)


        for tiles in to_visit:
            tiles = tuple(tiles)
            val = grid_cpy[tiles]
            _, neigh_tiles = get_neighbours(tiles, grid_cpy)
            num_black_tiles = sum([ 1 for x in neigh_tiles if x % 2 == 1])
            # print(tiles, val, num_black_tiles, neigh_tiles)
            if val % 2 == 1 and num_black_tiles in [0,3,4,5,6]: # Black tile
                grid[tiles] += 1 # flip the tiles
            elif val % 2 == 0 and num_black_tiles == 2: # white tile
                grid[tiles] += 1  

        print('Day %d, Black tiles %d' % (day, sum([ 1 for x in grid.values() if x % 2 == 1])) ) 


def main():
    input_file = 'D:\Projects\AdventOfCode2020\day24\input.txt'
    # input_file = 'D:\Projects\AdventOfCode2020\day24\sample_input.txt'
    # input_file = 'D:\Projects\AdventOfCode2020\day24\my_sample_input.txt'
    input_list = input_parser(input_file)
    
    # part 1
    grid = flip_tiles(input_list)
    
    # part 2
    simulate_live_art(grid, days=100)

if __name__ == "__main__":
    main()