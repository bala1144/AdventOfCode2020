from itertools import product
import copy

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n')

    early_time = int(input_list[0])
    bus_ids = [ int(x) for x in input_list[1].split(',') if x != 'x' ]
    inputs = (early_time, bus_ids)
    return inputs

def find_first_bus_diff(inputs):
    early_time = inputs[0]
    bus_ids = inputs[1]
    diffs = [ bus - (early_time % bus) for bus in bus_ids]
    min_diff =  min(diffs) * bus_ids[diffs.index(min(diffs))]
    return min_diff

# ************** insipred soltuion from our AOC group  ********************
def puzzle2(input_file):
    input_list = open(input_file).read().split()

    bus_ids = input_list[1].split(',')
    bus_ids = [int(id) if id !='x' else -1 for id in bus_ids]

    mult = bus_ids[0]
    slot = 0

    for i in range(1, len(bus_ids)):

        if bus_ids[i] == -1:
            continue
        while(True):
            slot += mult
            print('slot', slot)
            if not (slot + i) % bus_ids[i]:
                mult *= bus_ids[i]
                break
    
    return slot

def main():
    # input_file = 'D:\Projects\AdventOfCode2020\day13\sample_input.txt'
    input_file = 'D:\Projects\AdventOfCode2020\day13\input.txt'
    inputs = input_parser(input_file) 

    # puzzle 1
    print('Puzzle 1', find_first_bus_diff(inputs))

    # puzzle 2
     print('Puzzle w', puzzle2(input_file))

if __name__ == "__main__":
    # main()
    fn()