from itertools import product
import copy

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n')

    input_list = [ (line[0],  int(line[1:])) for line in input_list]
    return input_list

def find_manhattan_dist(input_list):
    """
    Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:
    
    """
    dirs_order = ['E','S','W','N']
    dist = {'E':0, 'N':0, 'S':0, 'W':0}

    facing_dir = 'E'
    for cmd, val in input_list:
        
        if 'F' == cmd:
            dist[facing_dir] += val
        elif 'E' == cmd:
             dist['E'] += val
        elif 'W' == cmd:
             dist['W'] += val
        elif 'N' == cmd: 
            dist['N'] += val
        elif 'S' == cmd:
             dist['S'] += val
        elif 'R' == cmd or  'L' == cmd :
            if 'L' in cmd:
                val = -val
            # change the dirs
            dir_order_index = int(dirs_order.index(facing_dir) + (val//90)) % 4
            facing_dir = dirs_order[dir_order_index] 

    print(dist)
    print('Manhattan distance',  abs(dist['E']-dist['W'])+ abs(dist['S']-dist['N'] ))

def find_manhattan_dist_way_pt_based(input_list):
    """
    the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position
    
    """
    dirs_order = ['E','S','W','N']
    ship_pos = {'E':0, 'S':0, 'W':0, 'N':0}
    way_pt_dir = [10,0,0,1] # E,S,W,N

    for cmd, val in input_list:
        if 'F' == cmd:
            # ship_pos = val
            ship_pos = {  k: (ship_pos[k] + way_pt_dir[i] * val) for i,k in enumerate(ship_pos.keys()) }
        elif 'E' == cmd:
             way_pt_dir[0] += val
        elif 'W' == cmd:
             way_pt_dir[2] += val
        elif 'N' == cmd: 
            way_pt_dir[3] += val
        elif 'S' == cmd:
             way_pt_dir[1] += val
        elif 'R' == cmd or  'L' == cmd :
            if 'R' in cmd:
                val = -val
            # change the dirs
            dir_order_index = (val//90) % 4
            new_way_pt_dir = [ way_pt_dir[i%4] for i in range(dir_order_index, dir_order_index+4)]
            way_pt_dir = new_way_pt_dir


    print(ship_pos)
    print('Manhattan ship_posance',  abs(ship_pos['E']-ship_pos['W'])+ abs(ship_pos['S']-ship_pos['N'] )

def main():
    # input_file = 'D:\Projects\AdventOfCode2020\day12\sample_input.txt'
    input_file = 'D:\Projects\AdventOfCode2020\day12\input.txt'
    instructions = input_parser(input_file) 
    # puzzle 1 
    find_manhattan_dist(instructions)
    # puzzle 2
    find_manhattan_dist_way_pt_based(instructions)

if __name__ == "__main__":
    main()