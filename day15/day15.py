from collections import defaultdict

def input_parser(input_file):
    with open(input_file) as f:
        input_list = f.read().split('\n')
    numbers = list(map(int, input_list[0].split(',')))

    return numbers

def sim_memory_game(start_numbers, Nth):
    """Simulate the memory game mentioned in the puzzle and return the nth number in the game
    """

    memory = defaultdict(int)

    # add the start numbers to the dict
    for i in range(0,len(start_numbers)):
        memory[start_numbers[i]] = (i+1) 
    
    # this is len(n) + 1th epoch 
    curr_num = 0
    for i in range(len(start_numbers)+2, Nth+1):

        if memory[curr_num] > 0:
            next_num = (i-1) - memory[curr_num]
        else:
            next_num = 0

        memory[curr_num] = (i-1)
        curr_num = next_num
        # print(i,curr_num, next_num)


    print(next_num)        


def main():
    input_file = 'D:\Projects\AdventOfCode2020\day15\sample_input.txt'
    numbers = input_parser(input_file) 
    print('Puzzle 1 out', im_memory_game(numbers, 30000000))

if __name__ == "__main__":
    main()