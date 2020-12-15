import re
from itertools import combinations 

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n')

    instruction_list = []
    for line in input_list: 
        if 'mask' in line:
           instruction_list.append(re.search("[X01]+", line).group())
        elif 'mem' in line:
            instruction_list.append(tuple(map(int,re.findall(r"\d+", line))))
        else:
            raise RuntimeError('Invalid instruction')
    return instruction_list

def set_nth_bit(val, bitPosition):
    return val | 1 << bitPosition

def reset_nth_bit(val, bitPosition):
    return val & ~(1 << bitPosition) 

def apply_mask(val, mask):
    """Apply mask similar to the following example

    value:  000000000000000000000000000000001011  (decimal 11)
    mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    result: 000000000000000000000000000001001001  (decimal 73)

    fn : copy the 1's on 0's from the mask to the input value and compute the resulting decimal val

    """
    for bitPosition, x in enumerate(mask[::-1]):
        if x == '1':
            val = set_nth_bit(val, bitPosition) # set bit
        elif x == '0':
            val = reset_nth_bit(val, bitPosition) # reset bit

    return val

def apply_mask_version2(val, mask):
    """Apply mask similar to the following example

    A version 2 decoder chip doesn't modify the values being written at all. Instead, 
    it acts as a memory address decoder. Immediately before a value is written to memory, 
    each bit in the bitmask modifies the corresponding bit of the destination memory address
     in the following way:

    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
    If the bitmask bit is X, the corresponding memory address bit is floating.


    fn : copy the 1's from the mask to the input value and compute the resulting decimal val

    """
    memory_diffs = []
    for bitPosition, x in enumerate(mask[::-1]):
        if x == '1':
            val = set_nth_bit(val, bitPosition) # set bit
        elif x == 'X':
            val = reset_nth_bit(val, bitPosition)
            memory_diffs.append(pow(2,bitPosition))
    
    memory_addrs = [ val + sum(com) for sub in range(len(memory_diffs)) for com in combinations(memory_diffs, sub + 1)] 
    memory_addrs.append(val) # adding the no-combination case
    return memory_addrs

def compute_memory_values(instruction_list):
    """ go thorugh the instruction provided and compute the values to be loaded to the memory
    """
    memory = {}
    current_mask  = None
    for instruction in instruction_list:
        if type(instruction) is str:
            current_mask = instruction
        else:
            addrs, val = instruction
            # print(instruction, apply_mask(val, current_mask))/
            memory[addrs] = apply_mask(val, current_mask)

    return memory

def compute_memory_values_version2(instruction_list):
    """ go thorugh the instruction provided and compute the values to be loaded to the memory
    """
    memory = {}
    current_mask  = None
    for instruction in instruction_list:
        if type(instruction) is str:
            current_mask = instruction
        else:
            addrs, val = instruction
            for addrs in apply_mask_version2(addrs, current_mask):
                memory[addrs] = val

    return memory

def main():
    # input_file = 'D:\Projects\AdventOfCode2020\day14\sample_input_part2.txt'
    input_file = 'D:\Projects\AdventOfCode2020\day14\input.txt'
    instruction_list = input_parser(input_file) 

    # puzzle 1
    memory = compute_memory_values(instruction_list)
    print('The sum of values in the dict = ', sum(memory.values()))

    # puzzle 2
    memory = compute_memory_values_version2(instruction_list)
    print('The sum of values in the dict = ', sum(memory.values()))

if __name__ == "__main__":
    main()