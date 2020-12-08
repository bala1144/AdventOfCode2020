import copy

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n')

    instruction_list = []
    for cmd in input_list:
        instruction, arg = cmd.split()
        instruction_list.append([instruction, int(arg)])

    return instruction_list

def find_first_infintite_loop_instruction(instruction_list):
    """  find the first occurence of the infinite loop """
    accumulator = 0   
    i = 0
    visited_pos = set()
    while i < len(instruction_list) and (i not in visited_pos) : 
        visited_pos.add(i)

        if 'jmp' == instruction_list[i][0]:
            i += instruction_list[i][1]
        elif 'acc' == instruction_list[i][0]:
            accumulator +=  instruction_list[i][1]
            i += 1
        else: # condition for nop
            i += 1  

    return accumulator, i

def fix_infinite_loop_instruction(instruction_list):
    """  fix the infinite loop by changing the instruction set between 'jmp' and 'nop' """
    
    i = 0
    while i < len(instruction_list):

        modified_instruciton_list =  copy.deepcopy(instruction_list)

        # find and replace the string set and check whether it terminate or not
        if 'jmp' == instruction_list[i][0]:
            modified_instruciton_list[i][0] = 'nop'
        elif 'nop' == instruction_list[i][0]:
            modified_instruciton_list[i][0] = 'jmp'

        accumulator, last_pos = find_first_infintite_loop_instruction(modified_instruciton_list)

        if last_pos == len(instruction_list):
            break
        i += 1 # increment the instruction set

    return accumulator

def main():
    input_file = 'D:\Projects\AdventOfCode2020\day8\input.txt'
    instruction_list = input_parser(input_file)
    
    # puzzle 1
    accumulator, _ = find_first_infintite_loop_instruction(instruction_list)
    print('Puzzle 1 Accumulator val = ',  accumulator)

    # puzzle 2
    accumulator = fix_infinite_loop_instruction(instruction_list)
    print('Puzzle 2 Accumulator val = ',  accumulator)

if __name__ == "__main__":
    main()
